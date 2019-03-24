import os
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .models import NewsCategory, News
from django.http import HttpResponse
from django.conf import settings


# Create your views here.
def index(request):
    return HttpResponse("北京理工的首页")


def index_news(request):
    # news = News.objects.all()[0:5]
    news = News.objects.all()
    page_num = News.objects.count()
    return render(request, "bjlg/index_news.html", {"page_num": page_num, "news": news})


# ==========================================================================================
# 打印验证码
def verifycode(request):
    # 引入绘图模块
    from PIL import Image, ImageDraw, ImageFont
    # 引入随机函数模块
    import random
    # 定义变量,用于画面的背景色,长宽高
    bgcolor = (random.randrange(20, 100), random.randrange(20, 100), random.randrange(20, 100))
    width = 100
    height = 50
    # 创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
        # 定义验证码的被选值
    str = '1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
    rand_str = ''
    for i in range(0, 4):
        rand_str += str[random.randrange(0, len(str))]
    # 构造字体对象
    font = ImageFont.truetype('/Users/cocao/Library/Fonts/STSONG.TTF', 40)

    # font = ImageFont.truetype(r'C:\Windows\Fonts\AdobeArabic-Bold.otf', 40)
    # 构造字体颜色
    fontcolor1 = (255, random.randrange(0, 255), random.randrange(0, 255))
    fontcolor2 = (255, random.randrange(0, 255), random.randrange(0, 255))
    fontcolor3 = (255, random.randrange(0, 255), random.randrange(0, 255))
    fontcolor4 = (255, random.randrange(0, 255), random.randrange(0, 255))

    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor1)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor2)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor3)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor4)
    # 释放画笔
    del draw
    request.session['verify'] = rand_str
    import io

    buf = io.BytesIO()
    # 将图片保存起来给浏览器
    im.save(buf, 'png')
    # 将内存的图片数据给客户端
    return HttpResponse(buf.getvalue(), 'image/png')


# ==========================================================================================
# 1,主页
def index_main(request):
    # 这里注意下/bjlg/test_red2
    username = request.session.get("name", "游客")
    pwd = request.session.get("pwd", "***")
    return render(request, "bjlg/index_main.html", {"username": username, "pwd": pwd})


# 2.登录如果登录有误把falg设置为Flase,重新登录
def to_login(request):
    flag = request.session.get("flag", True)
    str_msg = ""
    if flag == False:
        str_msg = "请重新输入"
    request.session.clear()
    return render(request, "bjlg/login.html", {"str_msg": str_msg})


# 3.登录页面,输入账号密码,验证码,正确跳主页,不正确再去登录
def login(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    # 下面是取验证码的
    verifycode = request.POST.get("verifycode")
    verify = request.session["verify"]

    # 这是为了回显,状态保持而做的,可以省略
    request.session["name"] = username
    request.session["pwd"] = password
    msg = "欢迎%s登录" % username
    if verify == verifycode:
        return render(request, "bjlg/index_main.html", {"msg": msg})
    else:
        request.session["flag"] = False
        return redirect("bjlg:to_login")


# 4.退出登录,清除session
def quit(requst):
    # 清除session
    logout(requst)  # 方法一
    # requst.session.clear() #方法二
    # requst.session.flush() 方法三
    return redirect("bjlg:index_main")


# ==========================================================================================
# 上传文件页面

def upfiles(request):
    msg = "hh"
    return render(request, "bjlg/upfiles.html", {"msg": msg})


def savefile(request):
    # 注意上传文件一定是post请求,所以先判断一下
    if request.method == "POST":
        up_file = request.FILES["file"]
        # 合成文件的路径
        filepath = os.path.join(settings.MEDIA_ROOT, up_file.name)
        # 文件复制读再写该目录
        with open(filepath, "wb") as fp:
            for info in up_file.chunks():
                fp.write(info)
        return HttpResponse("上传成功")
    else:
        return HttpResponse("上传失败")


# ==========================================================================================

# 分页
from django.core.paginator import Paginator


def newsPage(request, page):
    newsList = News.objects.all()
    # 把所有内容放分页插件,每页展示4个
    paginator = Paginator(newsList, 4)
    # 把第几页传递过去
    newsPage = paginator.page(page)
    return render(request, "bjlg/newsPage.html", {"newsPage": newsPage})


def ajaxNews(request):
    return render(request, "bjlg/ajaxNews.html")


# 导入以json数据格式返回
from django.http import JsonResponse


def ajaxNewsDetail(request):
    newsList=News.objects.all()[0:5]
    list=[]
    for news in newsList:
        list.append([news.title,news.author,news.updateDate])
    return JsonResponse({"data":list})