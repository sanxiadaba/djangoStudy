from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField(default=2)
    # 中途添加数据库时要设置默认值,也可以设置默认为空
    # size=models.IntegerField(default=2,null=True,blank=True)


class Department(models.Model):
    title = models.CharField(max_length=16)
