#入力されたパラメーターをそのまま返すwebフォーム

from flask import Flask,request

app = Flask(__name__)

#サーバーにアクセスがあった場合
@app.route('/')
def index():
    return """
            <html><body>
            <form action="/callback" method="GET">
              ワードを入力してください: <input type="text" name="name">
              <input type="submit" value="送信">
            </form>
            </body></html>
        """

# /callback へアクセスがあった時
@app.route('/callback')
def callback():
    # wordのパラメータを得る
    name = request.args.get('name')
    if name is None: name = '入力し直してください'
    # 適当な返答をする(デフォルトではwordのパラメーターをそのまま返す)
    return """
    <h1>{0}</h1>
    """.format(name)


if __name__ == '__main__':
    app.run()
