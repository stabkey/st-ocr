# Azure とStreamlitを用いた画像認識アプリ  
   
このアプリは、Azure OpenAIを利用して、画像に関する質問に答えるStreamlitアプリケーションです。アップロードされた画像に関する質問をAzure OpenAIを使って回答します。本READMEはAIによって作成されました。  
   
## 必要な環境変数  
   
アプリを実行する前に、以下の環境変数を設定する必要があります。これらの環境変数は、`.env`ファイルに保存します。  
   
```plaintext  
AZURE_OPENAI_API_KEY=your_azure_openai_api_key  
AZURE_OPENAI_ENDPOINT=your_azure_openai_endpoint  
AZURE_OPENAI_DEPLOYMENT=your_azure_openai_deployment  
AZURE_OPENAI_GPT4O_API_KEY=your_gpt4o_api_key  
AZURE_OPENAI_GPT4O_ENDPOINT=your_gpt4o_endpoint  
AZURE_COMPUTER_VISION_ENDPOINT=your_azure_computer_vision_endpoint  
AZURE_COMPUTER_VISION_KEY=your_azure_computer_vision_key  
```  
   
## 必要な依存関係  
   
以下のPythonパッケージが必要です：  
   
- streamlit  
- openai  
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
   
3. `.env`ファイルを作成し、必要な環境変数を設定します：  
   
```plaintext  
AZURE_OPENAI_API_KEY=your_azure_openai_api_key  
AZURE_OPENAI_ENDPOINT=your_azure_openai_endpoint  
AZURE_OPENAI_DEPLOYMENT=your_azure_openai_deployment  
AZURE_OPENAI_GPT4O_API_KEY=your_gpt4o_api_key  
AZURE_OPENAI_GPT4O_ENDPOINT=your_gpt4o_endpoint  
AZURE_COMPUTER_VISION_ENDPOINT=your_azure_computer_vision_endpoint  
AZURE_COMPUTER_VISION_KEY=your_azure_computer_vision_key  
```  
   
## 実行  
   
以下のコマンドでアプリを実行します：  
   
```sh  
streamlit run app.py  
```  
   
アプリケーションが起動したら、ブラウザで表示されるURLにアクセスして、画像をアップロードし、AIに関する質問を入力してください。Azure OpenAIとAzure Computer Visionを使用して、画像に関する質問に回答します。  
   
## アプリケーションの概要  
   
このアプリケーションは、ユーザーがアップロードした画像に対して質問を行い、その質問に対する回答を提供します。具体的な機能は以下の通りです：  
   
1. **画像のアップロード**: ユーザーはローカルから画像をアップロードします。  
2. **質問の入力**: ユーザーは画像に関する質問を入力します。  
3. **質問への回答**: Azure OpenAIサービスを使用して、画像に関する質問に回答します。  
   
## トラブルシューティング  
   
もしアプリケーションの実行中に問題が発生した場合は、以下の点を確認してください：  
   
- 環境変数が正しく設定されているか  
- 必要なPythonパッケージがすべてインストールされているか  
- Azureサービスのキーやエンドポイントが正しいか  
   
問題が解決しない場合は、プロジェクトのIssueトラッカーで詳細を報告してください。  
   
---  
   
このREADME.mdには、アプリケーションを実行するための初期設定に必要な手順がすべて含まれています。これにより、依存関係のインストールから環境変数の設定、アプリケーションの実行方法までをカバーしています。他の開発者がこのアプリケーションを簡単にセットアップして使用できるようになります。  
