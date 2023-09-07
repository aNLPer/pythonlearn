"""
根据intro部分的介绍我们知道，开发者只用编写一个函数func并以http响应函数，http请求信息为参数，函数func由wsgi调用。
在func中我们可以根据http请求信息获取用户请求路径，并将请求路径映射到不同的函数，从而使得我们web应用可以为用户提供
各种功能，如下：
def application(environ, start_response):
    method = environ['REQUEST_METHOD']
    path = environ['PATH_INFO']
    if method=='GET' and path=='/': # 请求路径1
        return handle_home(environ, start_response)
    if method=='POST' and path='/signin': # 请求路径2
        return handle_signin(environ, start_response)
    ...
但是这种写法代码维护成本较高，下面是Flask框架的例子
"""
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'

@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'

if __name__ == '__main__':
    app.run()