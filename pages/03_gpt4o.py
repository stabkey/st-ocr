import os  
import dotenv  
import streamlit as st  
from openai import AzureOpenAI  
from PIL import Image  
import base64  
  
# .envファイルを読み込む  
dotenv.load_dotenv()  
  
# Azure OpenAI のクライアントを作成する  
client = AzureOpenAI(  
    api_key=os.getenv("AZURE_OPENAI_GPT4O_API_KEY"),  
    api_version="2024-02-01",  
    azure_endpoint=os.getenv("AZURE_OPENAI_GPT4O_ENDPOINT")  
)  
  
# タイトルを表示する  
st.title("GPT-4oのテスト")  
  
# 説明文を表示する  
st.info("GPT-4oが画像に関する質問に答えます。")  
  
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
  
    # 画像をbase64形式に変換する  
    image_base64 = base64.b64encode(image_bytes).decode("utf-8")  
  
    # データURL形式に変換する  
    image_data_url = f"data:image/{uploaded_file.type.split('/')[-1]};base64,{image_base64}"  
  
    # ユーザーの入力を取得する  
    user_input = st.chat_input("画像に関する質問を入力してください。")  
  
    # チャットを送信した際の処理  
    if user_input:  
        # ユーザーが入力した検索キーワードを表示する  
        with st.chat_message("user"):  
            st.write(user_input)  
          
        # データソースから回答を得る  
        chat_completion = client.chat.completions.create(  
            model="gpt-4o",  
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
                                "url": image_data_url  
                            }  
                        },  
                        {  
                            "type": "text",  
                            "text": user_input  
                        }  
                    ]  
                }  
            ],  
            max_tokens=2000  
        )  
  
        # 結果を表示  
        with st.chat_message("assistant"):  
            st.write(chat_completion.choices[0].message.content)  
  
        # 履歴に追加する  
        st.session_state.history.append({"role": "user", "content": user_input})  
        st.session_state.history.append({"role": "assistant", "content": chat_completion.choices[0].message.content})  
