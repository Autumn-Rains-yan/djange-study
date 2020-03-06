from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse, render, redirect
from monitor import models


def index(request):
    return HttpResponse('Hello Monitor')


# orm操作数据库
def orm(request):
    # 添加数据
    # 1
    # models.UserInfo.objects.create(username='root', password='123')
    # 2
    # dict = {
    #     'username': 'lisi',
    #     'password': 'qwe'
    # }
    # models.UserInfo.objects.create(**dict)
    # 3
    # obj = models.UserInfo(username='zhangsan', password='123')
    # obj.save()

    # 查询数据
    # res = models.UserInfo.objects.all()
    # for info in res:
    #     print(info.username)
    #     print(info.password)
    # res = models.UserInfo.objects.filter(username='root')
    # print(res[0].password)

    # 修改数据
    # models.UserInfo.objects.filter(username='lisi').update(password='lisi123')

    # 删除数据
    # models.UserInfo.objects.filter(username='lisi').delete()
    return HttpResponse('orm')


# 登录
def login(request):
    error_msg = ''

    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        if username == '' or password == '':
            error_msg = '用户名或密码不能为空'
            return render(request, 'login.html', {'error_msg': error_msg})
        userinfos = models.UserInfo.objects.filter(username=username)
        if len(userinfos) != 0 and password == userinfos[0].password:
            return redirect(home)
        else:
            error_msg = '用户名或密码错误'
        # SQL操作
    return render(request, 'login.html', {'error_msg': error_msg})


# 首页
def home(request):
    error_msg = ''

    if request.method == 'POST':
        temp = {
            'username': request.POST.get('username', None),
            'age': request.POST.get('age', None),
            'gender': request.POST.get('gender', None),
            'password': request.POST.get('password', None)
        }

        if temp['username'] == '' or temp['password'] == '':
            error_msg = '用户名或密码不能为空'
        elif models.UserInfo.objects.filter(username=temp['username']):
            error_msg = '用户名已存在'
        else:
            models.UserInfo.objects.create(**temp)

    res = models.UserInfo.objects.all()
    for user_temp in res:
        if user_temp.age is None:
            user_temp.age = ''
        if user_temp.gender is None:
            user_temp.gender = ''
    return render(request, 'home.html', {'userList': res, 'error_msg': error_msg})


# 详情
def detail(request, *args, **kwargs):
    uid = kwargs['uid']
    res = models.UserInfo.objects.filter(id=uid)
    USER_INFO = res[0]
    if USER_INFO.age is None:
        USER_INFO.age = ''
    if USER_INFO.gender is None:
        USER_INFO.gender = ''
    return render(request, 'detail.html', {'user_list': USER_INFO})
