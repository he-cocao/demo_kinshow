#!/usr/bin/env python
# encoding: utf-8
"""
@version: Python 3.5.1
@author: cocao
@file: urls.py
@time: 2019/3/21 7:56 PM
"""

from django.urls import path
from . import views

app_name = "bjlg"
urlpatterns = [
    # 新版本可以直接在项目下urls下面配置url
    path('', views.index),
    path("index_news", views.index_news, name="index_news"),
    path("index_main/", views.index_main, name="index_main"),
    path("to_login/", views.to_login, name="to_login"),
    path("login/", views.login, name="login"),
    path("quit/", views.quit),
    # 显示验证码
    path("verifycode/", views.verifycode, name="verifycode"),
    path("upfiles", views.upfiles),
    path("savefile/", views.savefile, name="savefile"),
    path("newsPage/<int:page>", views.newsPage, name="newsPage"),
    path("ajaxNews", views.ajaxNews, name="ajaxNews"),
    path("ajaxNewsDetail/", views.ajaxNewsDetail, name="ajaxNewsDetail"),


]
