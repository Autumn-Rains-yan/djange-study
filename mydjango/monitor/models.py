from django.db import models


# Create your models here.

# 表名：monitor_userinfo
class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.CharField(max_length=3, blank=True, null=True)
    gender = models.CharField(max_length=16, blank=True, null=True)
    email = models.EmailField(max_length=32, blank=True, null=True)