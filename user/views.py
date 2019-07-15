import hashlib
import json
import time

import jwt
from django.http import JsonResponse
from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
from user.models import User

key = 'gra123456'
user_email = {}
def login_view(request):
    pass



def register_view(request):
    """
        注册逻辑处理方法
        :param request:
        :return: Json字符串
        """
    # 当前视图函数只接受post
    if request.method == 'GET':
        result = {'code':200, 'data':'get成功'}
        return JsonResponse(result)
    elif request.method == 'POST':
        json_str = request.body
        if not json_str:
            #对post行为没有数据提交过来时抛出异常
            result = {'code': 2002, 'error':'Please Post data'}
            return JsonResponse(result)
        json_obj = json.loads(json_str)
        #获取前端传过来的所有信息
        post_data_array = get_register_data(json_obj)
        result = check_post_info(post_data_array)
        if result:
            return JsonResponse(result)

        #检测用户是否已存在
        exist_user = User.objects.filter(username=post_data_array[0])
        if exist_user:
            result = {'code': 2003, 'error': 'The username is existed !!! '}
            return JsonResponse(result)

        #检测电话号是否存在
        exist_tel = User.objects.filter(tel=post_data_array[2])
        if exist_tel:
            result = {'code': 2003, 'error': 'The telephone is existed !!! '}
            return JsonResponse(result)

        #检测邮箱是否存在
        exist_email = User.objects.filter(email=post_data_array[4])
        if exist_email:
            result = {'code': 2003, 'error': 'The email is existed !!! '}
            return JsonResponse(result)

        h_p =  hashlib.sha1()
        h_p.update(post_data_array[1].encode())

        try:
            User.objects.create(username = post_data_array[0],
                                nickname = post_data_array[0],
                                password = h_p.hexdigest(),
                                tel = post_data_array[2],
                                address = post_data_array[3],
                                email = post_data_array[4],
                                category = post_data_array[5],
                                avatar = 'avatar/b04.jpg')
        except Exception as e:
            result = {'code': 2004, 'error': 'Create user failed!'}
            return JsonResponse(result)

        # 根据用户名 生成token
        token = make_token(post_data_array[0])
        result = {'code': 200, 'username': post_data_array[0], 'data': {'token': token.decode()}}
        return JsonResponse(result)

def forget_password_view(request):
    if request.method == 'POST':
        json_str = request.body
        if not json_str:
            # 对post行为没有数据提交过来时抛出异常
            result = {'code': 2002, 'error': 'Please Post data'}
            return JsonResponse(result)
        json_obj = json.loads(json_str)
        email = json_obj.get('email')
        try:
            User.objects.get(email=email)
        except Exception as e:
            result = {'code': 2010, 'error': 'The email is not exist!'}
            return JsonResponse(result)


        title = '垃圾找家---找回密码链接'
        exp_time = int(time.time())+3600
        payload = {'email':email,'exp':exp_time }
        encryption_time = jwt.encode(payload, key, algorithm='HS256')

        rest_url = 'http://127.0.0.1:5000/reset_password?exp_time='+ encryption_time.decode()

        message = '找回密码链接为:'+rest_url
        send_mail(title, message, '895004589@qq.com',
                  [email], fail_silently=False)

        result = {'code': 200, 'data':'邮件发送成功'}
        return JsonResponse(result)

def rest_password_view(request):

    if request.method == 'GET':
        get_exp_time = request.GET['exp_time']
        try:
            res = jwt.decode(get_exp_time, key, algorithms='HS256')
        except Exception as e:
            result = {'code': 200, 'data': '链接以失效'}
            return JsonResponse(result)
        user_email['email'] = res['email']
        result = {'code': 200}
        return JsonResponse(result)
    elif request.method == 'POST':
        email = user_email['email']
        try:
            user = User.objects.get(email=email)
        except Exception as e:
            result = {'code': 2010,'error':'The email is not exist!'}
            return JsonResponse(result)

        json_str = request.body
        if not json_str:
            # 对post行为没有数据提交过来时抛出异常
            result = {'code': 2002, 'error': 'Please Post data'}
            return JsonResponse(result)
        json_obj = json.loads(json_str)
        new_password = json_obj.get('new_password')
        h_p = hashlib.sha1()
        h_p.update(new_password.encode())
        user.password = h_p.hexdigest()
        user.save()
        result = {'code': 200,'data':'修改成功'}
        return JsonResponse(result)

def user_info_view(request):
    pass

def get_register_data(json_obj):
    '''
    获取所有前端使用json传过来的数据
    :param json_obj:json对象
    :return: 一个包含所有数据的数组
    '''
    username = json_obj.get('username')
    password = json_obj.get('password')
    tel = json_obj.get('tel')
    address = json_obj.get('address')
    email = json_obj.get('email')
    categotry = json_obj.get('category')
    return (username,password,tel,address,email,categotry)

def check_post_info(array):
    '''
    检查数据是否为空
    :param array: 需要检查数据的数组
    :return: 字典格式(code和报错信息)
    '''
    for data in array:
        if data == '':
            result = {'code': 2000, 'error': 'Please Entry Full Data'}
            return result



def make_token(username,expire = 3600*24):
    '''
    根据用户名生成token
    :param username:用户名
    :param expire:token存活的时间
    :return:
    '''
    now_t = time.time()
    payload = {'username':username,'exp': int(now_t + expire)}
    return jwt.encode(payload, key, algorithm='HS256')
