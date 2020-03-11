from django.contrib import admin

# Register your models here.

from monitor import models

admin.site.register(models.UserInfo)
