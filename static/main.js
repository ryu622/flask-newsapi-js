window.onload = function() {
    //送信ボタンが押されたときにイベントを設定
    document.getElementById('submit').addEventListener('click', function() {
        //getElement取得して定数に代入
    const keyword = document.getElementById('keyword').value;
    console.log(keyword);
    if (!keyword) {
        alert('Please enter a keyword!');
        return;
    }
    //fetchでapiを叩く
    fetch(`/api/news?keyword=${keyword}`)
    .then(response => response.json())
    .then(data => {
        if (data.status === 'ok' && data.data) {
            let articles = [];
            //ほしい項目だけリストに格納
            for (let i = 0; i < data.data.length; i++) {
                let article = data.data[i];
                console.log(article);
                articles.push({
                'title': article['title'],
                'description':article['description'],
                'image': article['image'],
                'url':article['url']
                });
            }
          console.log(articles); //コンソールに表示
          //HTMLにaddressを表示
          var box = document.getElementById('box');//取得
          box.innerHTML = articles.map(a => {
            return `
              <div style="margin-bottom:20px;">
                <p><a href="${a.url}" target="_blank"><strong>${a.title}</strong></a></p>
                <p>${a.description}</p>
                ${a.image ? `<img src="${a.image}" alt="image" style="max-width:300px;">` : ''}
              </div>`;
        }).join('');
        } else {
            console.log("エラー:", data.message);
          }
      })
      .catch(error => {
          console.log("通信エラー:", error);
        });
    });
  };