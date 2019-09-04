# -*- coding: utf-8 -*- 
# ===============================================================================
# @Name:         flaskdemo
# @Description:  
# @Author:       springbocai
# @Date:         2019/9/4
# ===============================================================================
import json

import requests
from flask import Flask, request

app = Flask(__name__)
# status code 200 500 401 404 ......
# 首页
@app.route('/')  # 接口地址
def index():
    # 接口本身
    dict_info = {"msg":"home"}
    # 字典形式转化为json
    json_info = json.dumps(dict_info)  # 导入json
    return json_info,202,{"content-type":"application/json"} # 这里新增定义的status code

# 登录页
@app.route('/login')  #接口地址
def login():
    # 接口本身
    # 接收请求数据
    username = request.args.get('username')
    pwd      = request.args.get('pwd')
    return json.dumps({"username":username,"msg":"OK"}),202,{"content-type":"application/json"}

@app.route('/test_api') # 接口地址
def test_api():
    # 访问测试的网址
    # 返回数据
    # python 访问网址，导入requests 库,这个不是flask自带的那个
    url = request.args.get('url')
    res = requests.get(url)
    return res.text

# web 服务器
if __name__ == '__main__':
    app.run()