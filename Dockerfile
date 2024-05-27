# ベースイメージとして公式のPythonイメージを使用  
FROM python:3.12  
  
# 作業ディレクトリを作成  
WORKDIR /app  
  
# ローカルのrequirements.txtをコンテナにコピー  
COPY requirements.txt /app/  
  
# 依存関係をインストール  
RUN pip install --no-cache-dir -r requirements.txt  
  
# アプリケーションのコードをコンテナにコピー  
COPY . /app  
  
# ストリームリットを実行するための環境変数を設定  
ENV STREAMLIT_SERVER_PORT=80  
  
# ストリームリットを起動  
CMD ["streamlit", "run", "app.py"]  
  
