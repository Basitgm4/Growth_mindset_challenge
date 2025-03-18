import streamlit as st
import pandas as pd
import io

# --- Helper Functions ---

def convert_excel_to_csv(file):
    try:
        df = pd.read_excel(file)
        csv_buffer = io.StringIO()
        df.to_csv(csv_buffer, index=False)
        return csv_buffer.getvalue()
    except Exception as e:
        st.error(f"Error converting Excel to CSV: {e}")
        return None

def convert_csv_to_csv(file):
    try:
        df = pd.read_csv(file)
        csv_buffer = io.StringIO()
        df.to_csv(csv_buffer, index=False)
        return csv_buffer.getvalue()
    except Exception as e:
        st.error(f"Error reading CSV: {e}")
        return None

def convert_text_to_csv(file):
    try:
        # Assuming tab-separated or comma-separated text
        content = file.read().decode('utf-8')
        lines = content.splitlines()
        if lines:
            # Try to infer delimiter (could be improved)
            if '\t' in lines[0]:
                df = pd.read_csv(io.StringIO(content), sep='\t', header=None, engine='python')
            elif ',' in lines[0]:
                df = pd.read_csv(io.StringIO(content), header=None, engine='python')
            else:
                st.warning("Could not automatically detect delimiter in the text file. Please ensure it's tab or comma separated.")
                return None
            csv_buffer = io.StringIO()
            df.to_csv(csv_buffer, index=False)
            return csv_buffer.getvalue()
        else:
            st.warning("The text file is empty.")
            return None
    except Exception as e:
        st.error(f"Error converting text to CSV: {e}")
        return None

def convert_word_to_csv(file):
    try:
        from docx import Document
        document = Document(file)
        data = []
        for table in document.tables:
            for row in table.rows:
                row_data = [cell.text for cell in row.cells]
                data.append(row_data)
        if data:
            df = pd.DataFrame(data)
            csv_buffer = io.StringIO()
            df.to_csv(csv_buffer, index=False, header=False)
            return csv_buffer.getvalue()
        else:
            st.warning("No tables found in the Word document.")
            return None
    except ImportError:
        st.error("Please install the 'python-docx' library to convert Word files: pip install python-docx")
        return None
    except Exception as e:
        st.error(f"Error converting Word to CSV: {e}")
        return None

# --- Streamlit App ---

st.title("Growth Mindset Challenge Hub")
st.write("Welcome! This app is designed to help you embrace challenges and track your growth. Let's start by converting some files!")

st.header("Document to CSV Converter")
st.write("Upload your document file below and we'll convert it to CSV format.")

uploaded_file = st.file_uploader("Upload a file", type=["txt", "csv", "xlsx", "docx"])

if uploaded_file is not None:
    file_name = uploaded_file.name
    file_extension = file_name.split('.')[-1].lower()

    st.write(f"You uploaded: `{file_name}`")

    if file_extension == "xlsx":
        csv_data = convert_excel_to_csv(uploaded_file)
        if csv_data:
            st.success("Excel file successfully converted to CSV!")
            st.download_button(
                label="Download CSV",
                data=csv_data,
                file_name=f"{file_name.split('.')[0]}.csv",
                mime="text/csv"
            )
    elif file_extension == "csv":
        csv_data = convert_csv_to_csv(uploaded_file)
        if csv_data:
            st.success("CSV file (re)processed successfully!")
            st.download_button(
                label="Download CSV",
                data=csv_data,
                file_name=file_name,
                mime="text/csv"
            )
    elif file_extension == "txt":
        csv_data = convert_text_to_csv(uploaded_file)
        if csv_data:
            st.success("Text file successfully converted to CSV!")
            st.download_button(
                label="Download CSV",
                data=csv_data,
                file_name=f"{file_name.split('.')[0]}.csv",
                mime="text/csv"
            )
    elif file_extension == "docx":
        csv_data = convert_word_to_csv(uploaded_file)
        if csv_data:
            st.success("Word document (tables) successfully converted to CSV!")
            st.download_button(
                label="Download CSV",
                data=csv_data,
                file_name=f"{file_name.split('.')[0]}.csv",
                mime="text/csv"
            )
    else:
        st.warning("Unsupported file format. Please upload a .txt, .csv, .xlsx, or .docx file.")

st.header("Take on a New Challenge!")
new_challenge = st.text_input("What challenge are you taking on today?")
if new_challenge:
    st.success(f"Great! Your new challenge is: '{new_challenge}'")
    # In a more advanced version, you could store this challenge.

st.sidebar.title("Growth Mindset Tips")
st.sidebar.info("""
Embrace challenges as opportunities for growth.
Believe in your ability to improve through dedication and hard work.
Learn from feedback and persist in the face of setbacks.
Celebrate effort and progress, not just outcomes.
""")
st.sidebar.markdown("[Learn more about Growth Mindset](https://www.mindsetworks.com/what-is-mindset)") # Example link