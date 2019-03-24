from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from .models import NewsCategory, News


# Create your views here.
# 这就是定义视图,接着要个URL映射器,配置在项目下的urls.py
def index(request):
    return HttpResponse("你好,我是第一个视图")


def number(request, num, number):
    return HttpResponse("这个是个带了数字参数的页面%d-%s" % (num, number))

def newCategoryInfo(request):
    # 去模型里取数据 注意这里的categoryObj是自定义的管理器
    newsCategoryList = NewsCategory.categoryObj.all()
    # 将数据传递给模板(html),模板在渲染给页面,将渲染好的页面返回给浏览器
    return render(request, "kinshow/newsCategory.html", {"newsCategory": newsCategoryList})


def newsInfo(request):
    # page是指当前页码,count表示一页展示几个数据
    # page=int(request.GET["page"])

    page=int(request.GET.get("page"))
    count = 3
    if (page):
        # newsList = News.newsObj.all()[(page1 - 1) * count:page1 * count]
        newsList = News.newsObj.filter(title__contains="明天")[(page - 1) * count:page * count]
        # 将数据传递给模板(html),模板在渲染给页面,将渲染好的页面返回给浏览器
        return render(request, "kinshow/news.html", {"news": newsList, "page": str(page)})
    else:
        return render(request,"kinshow/news.html",{"msg":"没有新闻了"})



# 根据新闻分类找出该分类所有新闻
def newsBycategory(request, id):
    # 根据id找到分类对象 注意这里的categoryObj是自定义的管理器
    category = NewsCategory.categoryObj.get(pk=id)
    # 根据这个分类找出所有新闻
    newsList = category.news_set.all()
    return render(request, "kinshow/news.html", {"news": newsList})

def test(request):
    return HttpResponse("咋就不行了")
