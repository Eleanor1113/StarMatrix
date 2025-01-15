from flask import Flask #引入套件
from flask import render_template
from flask import redirect
from flask import request
from datetime import datetime
from flask import session
from flask import url_for


app = Flask(__name__)

@app.route('/')
def hello_world():
    return redirect(url_for('login')) 
@app.route('/login')
def login():
    return render_template('login.html')#取得html丟回前端

@app.route('/account_info_post', methods = ['POST'])#資訊進router 做後續function
def post_info():
    username = request.values['username']
    pw = request.values['password']
    if username == 'jack' and pw == '1qaz':
        return redirect(url_for('result2'))
    else:
        return 'oops'
@app.route('/result')
def result2():
    # 可以傳遞更多用戶資料給result.html，如果需要的話
    return render_template('index2.html')

if __name__ == '__main__':
    app.run()