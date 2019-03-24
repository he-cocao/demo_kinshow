#!/usr/bin/env python
# encoding: utf-8
"""
@version: Python 3.5.1
@author: cocao
@file: urls.py
@time: 2019/3/19 11:15 PM
在新版中这个urls文件可以不用了
"""

from django.urls import path
from . import views

app_name="kinshow"
urlpatterns = [
    # 新版本可以直接在项目下urls下面配置url
    path('', views.index),
    path("<int:num>/<number>", views.number),
    path("newscategory", views.newCategoryInfo),
    path("news/<int:page>", views.newsInfo,name="news"),
    path("<id>", views.newsBycategory),
    path("test",views.test)
]
