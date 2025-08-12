import streamlit as st
from PyPDF2 import PdfReader
import os
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Create books directory
BOOKS_DIR = "scanned_books"
os.makedirs(BOOKS_DIR, exist_ok=True)

# Set up the page
st.set_page_config(page_title="📚 Chat With Your Textbook", layout="wide")
st.title("📚 Chat With Your Textbook")

# Simple function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    try:
        text = ""
        reader = PdfReader(pdf_path)
        total_pages = len(reader.pages)
        
        # Simple progress message
        progress_text = st.empty()
        progress_text.text(f"Processing {total_pages} pages...")
        
        # Process each page with a simple counter
        page_number = 1
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
            page_number = page_number + 1
        
        progress_text.empty()
        return text
    except Exception as e:
        st.error(f"Error extracting text from PDF: {str(e)}")
        return ""

# Upload section
st.header("📖 Upload a Book")
uploaded_file = st.file_uploader("Upload a PDF with digital text", type=["pdf"])

if uploaded_file is not None:
    try:
        with open("temp.pdf", "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        extracted_text = extract_text_from_pdf("temp.pdf")

        if not extracted_text.strip():
            st.error("No text found in this PDF. Please upload a PDF with digital text.")
        else:
            st.success(f"Successfully extracted {len(extracted_text)} characters of text!")
            book_name = st.text_input("Enter a name for this book")
            if st.button("Save Book"):
                if not book_name.strip():
                    st.error("Please enter a book name.")
                else:
                    book_path = os.path.join(BOOKS_DIR, f"{book_name.strip()}.txt")
                    with open(book_path, "w", encoding="utf-8") as f:
                        f.write(extracted_text)
                    st.success(f"Book '{book_name}' saved successfully!")
    except Exception as e:
        st.error(f"Error processing uploaded file: {str(e)}")

# Chat section
st.header("💬 Chat with Your Books")

# Get list of books from the directory
books = []
for f in os.listdir(BOOKS_DIR):
    if f.endswith(".txt"):
        # Remove the last 4 characters (.txt) to get just the book name
        book_name = f[:-4]
        books.append(book_name)

if not books:
    st.info("No books found. Please upload a book first.")
else:
    selected_book = st.selectbox("Choose a book to chat with:", books)
    book_path = os.path.join(BOOKS_DIR, f"{selected_book}.txt")
    
    with open(book_path, "r", encoding="utf-8") as f:
        book_content = f.read()

    # Initialize or reset chat history when:
    # 1. No chat history exists (first time), OR
    # 2. No current book is tracked, OR  
    # 3. User switched to a different book
    # This ensures each book gets its own conversation context
    if "chat_history" not in st.session_state or "current_book" not in st.session_state or st.session_state.current_book != selected_book:
        st.session_state.chat_history = [
            {"role": "system", "content": f"You are a helpful assistant that answers questions based on the following book:\n\n{book_content}"}
        ]
        st.session_state.current_book = selected_book

    # Display chat history
    for msg in st.session_state.chat_history[1:]:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Chat input
    if user_question := st.chat_input("Ask a question about the book"):
        st.session_state.chat_history.append({"role": "user", "content": user_question})
        with st.chat_message("user"):
            st.markdown(user_question)

        with st.chat_message("assistant"):
            with st.spinner("Generating response..."):
                response = openai.chat.completions.create(
                    model="gpt-4o",
                    messages=st.session_state.chat_history,
                    temperature=0.2
                )
                answer = response.choices[0].message.content
                st.markdown(answer)
                st.session_state.chat_history.append({"role": "assistant", "content": answer}) 