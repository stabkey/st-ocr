import os  
import dotenv  
import streamlit as st  
from azure.core.credentials import AzureKeyCredential  
from azure.ai.formrecognizer import DocumentAnalysisClient  
  
# 環境変数の読み込み  
dotenv.load_dotenv()  
endpoint = os.getenv("FORM_RECOGNIZER_ENDPOINT")  
key = os.getenv("FORM_RECOGNIZER_KEY")  
  
# Document Analysis Client の設定  
credential = AzureKeyCredential(key)  
document_analysis_client = DocumentAnalysisClient(endpoint, credential)  
  
def analyze_pdf(file_path):  
    try:  
        with open(file_path, "rb") as f:  
            poller = document_analysis_client.begin_analyze_document("prebuilt-document", document=f)  
            result = poller.result()  
        return result  
    except Exception as e:  
        st.error(f"An error occurred: {e}")  
        return None  
  
# Streamlit アプリの設定  
st.title("PDF OCR with Azure AI Document Intelligence")  
  
uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])  
  
if uploaded_file is not None:  
    # ファイルを保存  
    with open("uploaded_file.pdf", "wb") as f:  
        f.write(uploaded_file.getbuffer())  
  
    # PDF を解析  
    with st.spinner("Analyzing PDF..."):  
        result = analyze_pdf("uploaded_file.pdf")  
  
    if result is not None:  
        # 結果を表示  
        st.write("Extracted Text:")  
  
        # 各ページを折りたたみセクションで表示  
        for page in result.pages:  
            with st.expander(f"Page {page.page_number}"):  
                page_text = "\n".join([line.content for line in page.lines])  
                st.text_area(f"Text from Page {page.page_number}", value=page_text, height=200)  
  
        # デバッグ情報の表示  
        with st.expander("Debug Info:"):  
            st.write(f"Total pages: {len(result.pages)}")  
            for page in result.pages:  
                st.write(f"Page {page.page_number} has {len(page.lines)} lines")  
    else:  
        st.error("Failed to analyze the PDF.")  
