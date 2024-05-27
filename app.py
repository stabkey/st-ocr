import streamlit as st  
from azure.cognitiveservices.vision.computervision import ComputerVisionClient  
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes  
from msrest.authentication import CognitiveServicesCredentials  
import time  
from PIL import Image  
import io  
import dotenv  
import os  
  
# .envファイルを読み込む  
dotenv.load_dotenv()  
  
# Azure AI VisionのAPIキーとエンドポイントを環境変数から取得  
subscription_key = os.getenv("AZURE_COMPUTER_VISION_KEY")  
endpoint = os.getenv("AZURE_COMPUTER_VISION_ENDPOINT")  
  
# ComputerVisionClientの作成  
computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))  
  
# Streamlitアプリのヘッダー  
st.title("Azure AI Vision OCR")  

# アプリの説明
st.info("画像に含まれるテキストを読み取ります。")
  
# 画像ファイルのアップロード  
uploaded_file = st.file_uploader("画像ファイルをアップロードしてください", type=["jpg", "jpeg", "png"], key="file_uploader_1")  
  
if uploaded_file is not None:  
    # 画像を表示  
    image = Image.open(uploaded_file)  
    st.image(image, caption='アップロードされた画像', use_column_width=True)  
  
    # 画像ファイルをバイト形式で読み込む  
    image_bytes = uploaded_file.getvalue()  # バイトデータを取得  
  
    # バイトオブジェクトをバイトストリームに変換  
    image_stream = io.BytesIO(image_bytes)  # 修正ポイント  
  
    # OCRを実行  
    st.write("OCRを実行中...")  
    try:  
        ocr_result = computervision_client.read_in_stream(image_stream, raw=True)  # 修正ポイント  
  
        # 操作IDを取得  
        operation_location = ocr_result.headers["Operation-Location"]  
        operation_id = operation_location.split("/")[-1]  
  
        # 操作が完了するまで待機  
        while True:  
            result = computervision_client.get_read_result(operation_id)  
            if result.status not in ['notStarted', 'running']:  
                break  
            time.sleep(1)  
  
        # 結果を表示  
        st.write("OCR結果:")  
        if result.status == OperationStatusCodes.succeeded:  
            ocr_text = ""  
            for text_result in result.analyze_result.read_results:  
                for line in text_result.lines:  
                    ocr_text += line.text + "\n"  
            st.code(ocr_text, language='text')  
    except Exception as e:  
        st.error(f"OCR処理中にエラーが発生しました: {e}")  
