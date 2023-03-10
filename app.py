from flask import Flask
#static:图片，css,js文件
#templates:html网页
#app.py:控制器
app = Flask(__name__)
"""
前端向后端发送请求：
1.http://ip.端口号/action?k1=v1&k2=v2
2.http://ip.端口号/action
后端向前端：
1.返回文本，网页
2.异步：json格式的数据
"""
@app.route("/")
def index():
    return "OK"
app.run()