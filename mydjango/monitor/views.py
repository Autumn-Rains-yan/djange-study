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
            return redirect('/home')
        else:
            error_msg = '用户名或密码错误'
    return render(request, 'login.html', {'error_msg': error_msg})

USER_LIST = [
    {'username': 'luoyan', 'age': 23, 'gender': 'male'}
]

for i in range(1, 10):
    temp = {'username': 'luoyan'+str(i), 'age': 23+i, 'gender': 'male'}
    USER_LIST.append(temp)


def home(request):
    if request.method == 'POST':
        temp = {
            'username': request.POST.get('username', None),
            'age': request.POST.get('age', None),
            'gender': request.POST.get('gender', None)
        }
        USER_LIST.append(temp)
    return render(request, 'home.html', {'userList': USER_LIST})
