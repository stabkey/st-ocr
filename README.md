# GPT-4-Turbo Vision アプリ  
   
このアプリは、Azure OpenAIとAzure Blob Storageを利用して、画像に関する質問に答えるStreamlitアプリケーションです。アップロードされた画像をAzure Blob Storageに保存し、その画像に関する質問をAzure OpenAIを使って回答します。  
   
## 必要な環境変数  
   
アプリを実行する前に、以下の環境変数を設定する必要があります。これらの環境変数は、`.env`ファイルに保存します。  
   
```plaintext  
AZURE_OPENAI_API_KEY=your_azure_openai_api_key  
AZURE_OPENAI_ENDPOINT=your_azure_openai_endpoint  
AZURE_OPENAI_DEPLOYMENT=your_azure_openai_deployment  
AZURE_COMPUTER_VISION_ENDPOINT=your_azure_computer_vision_endpoint  
AZURE_COMPUTER_VISION_KEY=your_azure_computer_vision_key  
AZURE_STORAGE_CONNECTION_STRING=your_azure_storage_connection_string  
AZURE_STORAGE_CONTAINER_NAME=your_azure_storage_container_name  
```  
   
## 必要な依存関係  
   
以下のPythonパッケージが必要です：  
   
- streamlit  
- openai  
- azure-storage-blob  
- azure-cognitiveservices-vision-computervision  
- msrest  
- python-dotenv  
- pillow  
   
## インストール  
   
1. リポジトリをクローンします：  
   
```sh  
git clone https://github.com/your-repository.git  
cd your-repository  
```  
   
2. 必要なPythonパッケージをインストールします：  
   
```sh  
pip install -r requirements.txt  
```  
   
`requirements.txt`は以下の内容です：  
   
```plaintext  
streamlit  
openai  
azure-storage-blob  
azure-cognitiveservices-vision-computervision  
msrest  
python-dotenv  
pillow  
```  
   
3. `.env`ファイルを作成し、必要な環境変数を設定します：  
   
```plaintext  
AZURE_OPENAI_API_KEY=your_azure_openai_api_key  
AZURE_OPENAI_ENDPOINT=your_azure_openai_endpoint  
AZURE_OPENAI_DEPLOYMENT=your_azure_openai_deployment  
AZURE_COMPUTER_VISION_ENDPOINT=your_azure_computer_vision_endpoint  
AZURE_COMPUTER_VISION_KEY=your_azure_computer_vision_key  
AZURE_STORAGE_CONNECTION_STRING=your_azure_storage_connection_string  
AZURE_STORAGE_CONTAINER_NAME=your_azure_storage_container_name  
```  
   
## 実行  
   
以下のコマンドでアプリを実行します：  
   
```sh  
streamlit run app.py  
```  
   
アプリケーションが起動したら、ブラウザで表示されるURLにアクセスして、画像をアップロードし、AIに関する質問を入力してください。Azure OpenAIとAzure Computer Visionを使用して、画像に関する質問に回答します。  
```  
   
このREADME.mdには、アプリケーションを実行するための初期設定に必要な手順がすべて含まれています。これにより、依存関係のインストールから環境変数の設定、アプリケーションの実行方法までをカバーしています。