import json

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

def login_view(request):
    pass

def register_view(request):
    """
        注册逻辑处理方法
        :param request:
        :return: Json字符串
        """
    if request.method == 'GET':
        result = {'code': 200, 'data': 'get success'}
        return JsonResponse(result)
    elif request.method == 'POST':
        json_str = request.body
        json_obj = json.loads(json_str)
        # 获取用户名和密码
        hname = json_obj.get('hname')
        hpwd = json_obj.get('hpwd')
        tel = json_obj.get('tel')
        address = json_obj.get('address')
        email = json_obj.get('email')
        print('hname:%s,hpwd:%s,tel:%s,address:%s,email:%s'
              %(hname,hpwd,tel,address,email))
        result = {'code': 200, 'data': 'post success'}
        return JsonResponse(result)


def forget_password_view(request):
    pass

def user_info_view(request):
    pass

