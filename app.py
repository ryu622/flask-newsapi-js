import requests
from flask import Flask,render_template,request
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
    #HTMLから変数を取得
    keyword=request.args.get("keyword")
    page = request.args.get("page", default=1, type=int)
    #先にリストを定義しておく
    articles=[]
    #キーワードが空でなければ処理
    if keyword:
        #クエリパラメータ
        params = {
                'q': keyword,
                'language': 'en',
                'pageSize': 5,
                'page': page,
                'apiKey': app.config['MY_APIKEY']
            }
        #apiにリクエストを送る
        res = requests.get('https://newsapi.org/v2/everything', params=params)
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
    return render_template('index.html',articles=articles,keyword=keyword,page=page)




#実行
if __name__=='__main__':
    app.run()


