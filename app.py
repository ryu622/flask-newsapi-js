import requests
from flask import Flask,render_template,request ,jsonify
import os
from dotenv import load_dotenv

# 環境変数に設定したAPIKeyを使うために.envファイルを読み込む
load_dotenv()


#インスタンス生成
app=Flask(__name__)

app.config['MY_APIKEY'] =os.getenv('MY_APIKEY')

#ルーティング
@app.route('/')
def index():
    return render_template('index.html')

#API
@app.route('/api/news')
def API():
    keyword = request.args.get('keyword')
    
    # キーワードが空の場合、エラーメッセージを返す
    if not keyword:
        return jsonify({
            'status': 'error',
            'message': 'Keyword is required'
        })

    #先にリストを定義しておく
    articles=[]
    #キーワードが空でなければ処理
    if keyword:
        #クエリパラメータ
        params = {
            'q': keyword,
            'language': 'en',
            'pageSize': '5',
            'apiKey': app.config['MY_APIKEY']
           }
        #apiにリクエストを送る
        res = requests.get('https://newsapi.org/v2/everything',params=params)
        #json形式で受け取る
        res_json = res.json()
        #ほしい項目だけリストに格納
        for article in res_json['articles']:
            articles.append({
        'title': article['title'],
        'description':article['description'],
        'image': article['urlToImage'],
        'url':article['url']
        })
        print(articles)
    else:
        print('準備OK')
    return jsonify({
    'status': 'ok',
    "message": "取得成功",
    'data': articles})




#実行
if __name__=='__main__':
    app.run()


