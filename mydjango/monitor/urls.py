from django.contrib import admin
from django.urls import path, re_path, include
from monitor import views

urlpatterns = [
    path('index/', views.index),
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('orm/', views.orm),
    re_path('detail/(?P<uid>\d+)/', views.detail)
]