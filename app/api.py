from flask import Flask,request

#创建一个服务，赋值给app
app=Flask(__name__)

#指定接口访问的路径和支持的请求
@app.route('/HelloWorld',methods=['post','get'])
#请求后，直接拼接入参方式
def get_ss():
    name= '2019'
    return 'hello world,'+name

app.run(host='0.0.0.0',port=8880,debug=True)

#windows就一个网卡，可以不写，linux有多个网卡，写成0.0.0.0可以接受任意网卡信息
