import streamlit as st
from PyPDF2 import PdfReader
from pdf2image import convert_from_path
from PIL import Image
import requests
import base64
import os
import io
import openai
from dotenv import load_dotenv
import tiktoken

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
OPENAI_API_URL = "https://api.openai.com/v1/chat/completions"

BOOKS_DIR = "scanned_books"
os.makedirs(BOOKS_DIR, exist_ok=True)

st.set_page_config(page_title="📚 Chat With Your Textbook", layout="wide")
st.title("📚 Chat With Your Textbook")

menu = ["Upload New Book", "Chat with Book"]
choice = st.sidebar.radio("Menu", menu)

# Vision OCR helper
def extract_text_with_gpt4o(image):
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    image_bytes = buffered.getvalue()
    image_base64 = base64.b64encode(image_bytes).decode("utf-8")

    headers = {
        "Authorization": f"Bearer {openai.api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "gpt-4o",
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{image_base64}"}},
                    {"type": "text", "text": "Extract all readable text from this image."}
                ]
            }
        ],
        "max_tokens": 1000
    }

    response = requests.post(OPENAI_API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"[Error {response.status_code}] {response.text}"

# PDF text extractor
def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        reader = PdfReader(pdf_path)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    except Exception as e:
        st.error(f"Failed to extract text from PDF: {e}")
    return text

# Token counter
def count_tokens(text, model="gpt-4o"):
    encoding = tiktoken.encoding_for_model(model)
    return len(encoding.encode(text))

if choice == "Upload New Book":
    uploaded_file = st.file_uploader("Upload a scanned or text-based PDF", type=["pdf"])
    if uploaded_file is not None:
        with open("temp.pdf", "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.info("Extracting text from PDF...")
        extracted_text = extract_text_from_pdf("temp.pdf")

        if not extracted_text.strip():
            st.warning("No embedded text found. Using GPT-4o Vision OCR...")
            try:
                images = convert_from_path("temp.pdf", dpi=100)
                for i, image in enumerate(images):
                    st.write(f"Processing page {i+1}...")
                    image.thumbnail((1024, 1024), Image.Resampling.LANCZOS)
                    extracted = extract_text_with_gpt4o(image)
                    extracted_text += extracted + "\n\n"
            except Exception as e:
                st.error(f"Error converting PDF to images: {e}")

        st.subheader("Extracted Text")
        st.text_area("Text from PDF", extracted_text, height=300)

        book_name = st.text_input("Enter a name for this book (unique)")
        if st.button("Save Book"):
            if not book_name.strip():
                st.error("Please enter a valid book name.")
            else:
                book_path = os.path.join(BOOKS_DIR, f"{book_name.strip()}.txt")
                if os.path.exists(book_path):
                    st.warning("A book with this name already exists. Please choose a different name.")
                else:
                    with open(book_path, "w", encoding="utf-8") as f:
                        f.write(extracted_text)
                    st.success(f"Book '{book_name}' saved successfully!")

elif choice == "Chat with Book":
    books = [f[:-4] for f in os.listdir(BOOKS_DIR) if f.endswith(".txt")]
    if not books:
        st.info("No books found. Please upload a book first.")
    else:
        selected_book = st.selectbox("Choose a book to chat with:", books)
        book_path = os.path.join(BOOKS_DIR, f"{selected_book}.txt")
        with open(book_path, "r", encoding="utf-8") as f:
            book_content = f.read()

        tokens = count_tokens(book_content)
        max_tokens_limit = 120000

        if tokens > max_tokens_limit:
            st.error(f"Book content too large for the model ({tokens} tokens). Please shorten or split the book.")
        else:
            st.caption(f"Book length: {len(book_content)} characters (~{tokens} tokens)")

            # Initialize or update chat history when book changes
            if "chat_history" not in st.session_state or "current_book" not in st.session_state or st.session_state.current_book != selected_book:
                st.session_state.chat_history = [
                    {"role": "system", "content": f"You are a helpful assistant that answers questions based on the following book:\n\n{book_content}"}
                ]
                st.session_state.current_book = selected_book

            for msg in st.session_state.chat_history[1:]:
                with st.chat_message(msg["role"]):
                    st.markdown(msg["content"])

            if user_question := st.chat_input("Ask a question about the book"):
                st.session_state.chat_history.append({"role": "user", "content": user_question})
                with st.chat_message("user"):
                    st.markdown(user_question)

                with st.chat_message("assistant"):
                    with st.spinner("Generating response..."):
                        try:
                            response = openai.chat.completions.create(
                                model="gpt-4o",
                                messages=st.session_state.chat_history,
                                temperature=0.2
                            )
                            answer = response.choices[0].message.content
                            st.markdown(answer)
                            st.session_state.chat_history.append({"role": "assistant", "content": answer})
                        except Exception as e:
                            st.error(f"OpenAI API error: {e}")
