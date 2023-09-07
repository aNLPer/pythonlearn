"""
根据app.py中使用字符串拼接的方式构造页面信息并返回的方式编写webapp，代码维护性太低了，因此我们需要使用模板。
模板就是，我们预先定义好页面的大致结构，然后将数据嵌入进去即可。这就是传说中的：
MVC：Model-View-Controller，中文名“模型-视图-控制器”。

Python处理URL的函数就是C：Controller，Controller负责业务逻辑，比如检查用户名是否存在，取出用户信息等等；
包含变量{{ name }}的模板就是V：View，View负责显示逻辑，通过简单地替换一些变量，View最终输出的就是用户看到的HTML。
MVC中的Model在哪？Model是用来传给View的，这样View在替换变量的时候，就可以从Model中取出相应的数据

Flask通过render_template()函数来实现模板的渲染。和Web框架类似，Python的模板也有很多种。
Flask默认支持的模板是jinja2，且默认模板文件夹为templates，所以我们需要安装jinja2,并把模板放入templates文件夹下
"""
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    print("home")
    return render_template('home.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username=='admin' and password=='password':
        return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='Bad username or password', username=username)

if __name__ == '__main__':
    app.run()