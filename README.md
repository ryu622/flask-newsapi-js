#タイトル 
flask-newsapi-js

#概要・背景 
apiを作ってフロントエンドとバックエンドに分けた開発の練習としてニュース検索アプリを作成した。バックエンドはFlaskでapiを作成し、フロントエンドはJavaScriptで作成したapiを叩くことでページの動的更新を実現した。まだ、UIは製作途中であり随時改善していく予定である。このアプリ作成の過程でJavaScriptによるfetchの方法やFlaskでapiを作ることの基礎を学べた。なお、APIキーはセキュリティのため.envフォルダに入れ.gitignoreとした。次はページ更新機能を実装する予定である。

#インストール方法 git clone https://github.com/ryu622/flask-newsapi-js.git cd　flask-newsapi-js  pip install -r requirements.txt

#使用方法 入力欄に検索語句を入れると、ニュースが検索されます。

#機能一覧 ・NEWSapiを叩いてキーワードを含むニュースを取得 ・（SQLインジェクション対策として）バリデーション機能

#開発環境・技術スタック 
フロントエンド：HTML,CSS,JavaScript
バックエンド：Python,Flask

#ライセンス MIT License

#作成者 https://github.com/ryu622
