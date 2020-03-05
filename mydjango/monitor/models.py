from django.db import models

# Create your models here.

# 表名：monitor_userinfo
class UserInfo(models.Model):

    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)

