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
        result = {'code': 200, 'data': 'post success'}
        return JsonResponse(result)


def forget_password_view(request):
    pass

def user_info_view(request):
    pass

