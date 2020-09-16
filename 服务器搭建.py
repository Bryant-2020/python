from wsgiref.simple_server import make_server
import json

def show_index():
    return '欢迎访问'
def show_demo():
    return json.dumps({'name':'zhangsan'})
def show_register():
    with open('test.txt','r',encoding='utf8') as file:
        return file.read()

url={'/':show_index,
     '/demo':show_demo,
     '/register':show_register}

def demo_app(environ,start_response):
    #第0个参数，请求路径相关的环境
    #第1个参数，函数，返回响应头
    path=environ['PATH_INFO']
    status_code='200 OK'#默认状态码：200
    method=url.get(path)
    print(method)
    if method:
        response=method()
    else:
        status_code='404 Not Found'
        response='对不起，页面不存在'

    start_response(status_code,[('content-type','text/html;charset=utf8')])
    return [response.encode('utf8')]#列表返回元素:给浏览器的数据

if __name__=='__main__':
    httpd=make_server('',8080,demo_app)
    sa=httpd.socket.getsockname()
    print('Server HTTP on',sa[0],'port',sa[1],'...')
    #代码作用：打开电脑浏览器，并在浏览器输入
    #import webbrowser
    #webbrowser.open()

    httpd.handle_request()#处理一次请求