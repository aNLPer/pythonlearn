"""
一个Web应用的本质就是：
    1.浏览器发送一个HTTP请求；（由浏览器完成）
    2.服务器收到请求；（web服务器软件实现）
    3.服务器生成一个HTML文档；（业务代码）
    4.服务器把HTML文档作为HTTP响应的Body发送给浏览器；（web服务器软件实现）
    5.浏览器收到HTTP响应，从HTTP Body取出HTML文档并显示。（由浏览器完成）
"""

def application(environ, start_response):
    """
    Web开发者实现的一个函数，可以响应HTTP请求，由web服务器软件调用，可以看作web应用的入口函数
    :param environ: 包含所有HTTP请求信息的dict对象
    :param start_response: 发送HTTP响应的函数
    :return:
    """
    start_response('200 OK', [('Content-Type', 'text/html')]) # 发送了HTTP响应的Header
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode("utf-8")]