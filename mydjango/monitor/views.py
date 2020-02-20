from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse, render, redirect

def index(request):
    return HttpResponse('Hello Monitor')

def login(request):

    error_msg = ''

    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        print(username)
        if username == 'root' and password == '123':
            return redirect('https://www.baidu.com/')
        else:
            error_msg = '用户名或密码错误'
    return render(request, 'login.html', {'error_msg': error_msg})
