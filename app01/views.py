from django.shortcuts import render,HttpResponse

# Create your views here.
from app01.models import User


def index(request):
    return HttpResponse("欢迎使用")

def tImg(request):
    return render(request,"test01.html")


def tpl(request):
    info={"name":"张三","salary":1000}
    return render(request,"tpl.html",{"n1":info})


def orm(request):
    # 新建数据
    # User.objects.create(name="张三",age=12,password="123456")

    # 删除数据
    # 删除指定数据
    # User.objects.filter(id=1).delete()
    # 删除全部数据
    # User.objects.all().delete()

    # 获取数据

    return HttpResponse("操作数据库")
