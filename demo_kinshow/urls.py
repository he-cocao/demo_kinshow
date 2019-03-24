"""demo_kinshow URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    # 解决找不到favicon.ico报错信息的
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico')),
    path('admin/', admin.site.urls),  # 就是站点管理的那个url,跳到站点管理的视图

    path("kinshow/", include("kinshow.urls", namespace="kinshow")),  # 注册app中的url假如同一个app有俩个实例,有个命名空间namespace="kinshow"
    path("bjlg/", include("bjlg.urls", namespace="bjlg")),
    path("ueditor/", include("DjangoUeditor.urls"))

    # 新版本可以直接在项目下urls下面配置url
    # path('', views.index),

]
