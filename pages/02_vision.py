import os  
import dotenv  
import streamlit as st  
from openai import AzureOpenAI  
from PIL import Image  
from azure.storage.blob import BlobServiceClient
  
# .envファイルを読み込む  
dotenv.load_dotenv()  
  
# Azure OpenAI のクライアントを作成する  
client = AzureOpenAI(  
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
    api_version="2024-02-01",  
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")  
)  
  
# タイトルを表示する  
st.title("GPT-4-Turbo Vision のテスト")  
  
# 説明文を表示する  
st.info("AIが画像に関する質問に答えます。")  
  
# チャットの履歴がない場合は、履歴を初期化する  
if "history" not in st.session_state:  
    st.session_state.history = []  
  
# 履歴を表示する  
for chat in st.session_state.history:  
    with st.chat_message(chat["role"]):  
        st.write(chat["content"])  
  
# 画像ファイルのアップロード  
uploaded_file = st.file_uploader("画像ファイルをアップロードしてください", type=["jpg", "jpeg", "png"])  
  
if uploaded_file is not None:  
    # 画像を表示  
    image = Image.open(uploaded_file)  
    st.image(image, caption='アップロードされた画像', use_column_width=True)  
  
    # 画像をバイト形式で読み込む  
    image_bytes = uploaded_file.getvalue()  
  
    # Azure Blob Storage にアップロードする  
    blob_service_client = BlobServiceClient.from_connection_string(os.getenv("AZURE_STORAGE_CONNECTION_STRING"))  
    container_name = os.getenv("AZURE_STORAGE_CONTAINER_NAME")  
    blob_name = uploaded_file.name  
  
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)  
    blob_client.upload_blob(image_bytes, overwrite=True)  
  
    # Blob の URL を取得する  
    blob_url = f"https://{blob_service_client.account_name}.blob.core.windows.net/{container_name}/{blob_name}"  
    st.write(f"Blob URL: {blob_url}")  
  
    # ユーザーの入力を取得する  
    user_input = st.chat_input("画像に関する質問を入力してください。")  
  
    # チャットを送信した際の処理  
    if user_input:  
        # ユーザーが入力した検索キーワードを表示する  
        with st.chat_message("user"):  
            st.write(user_input)  
          
        # データソースから回答を得る  
        chat_completion = client.chat.completions.create(  
            model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),  
            messages=[  
                {  
                    "role": "system",  
                    "content": "画像の内容に基づいて以下の質問に答えてください",  
                },  
                {  
                    "role": "user",  
                    "content": [  
                        {  
                            "type": "image_url",  
                            "image_url": {  
                                "url": blob_url  
                            }  
                        },  
                        {  
                            "type": "text",  
                            "text": user_input  
                        }  
                    ]  
                }  
            ],  
            extra_body={  
                "data_sources": [  
                    {  
                        "type": "AzureComputerVision",  
                        "parameters": {  
                            "endpoint": os.getenv("AZURE_COMPUTER_VISION_ENDPOINT"),  
                            "key": os.getenv("AZURE_COMPUTER_VISION_KEY")  
                        }  
                    }  
                ],  
                "enhancements": {  
                    "ocr": {  
                        "enabled": True  
                    },  
                    "grounding": {  
                        "enabled": True  
                    }  
                }  
            },  
            max_tokens=2000  
        )  
  
        # 結果を表示  
        with st.chat_message("assistant"):  
            st.write(chat_completion.choices[0].message.content)  
  
        # 履歴に追加する  
        st.session_state.history.append({"role": "user", "content": user_input})  
        st.session_state.history.append({"role": "assistant", "content": chat_completion.choices[0].message.content})  

