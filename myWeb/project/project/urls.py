#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import sys
# sys.path.append("..")
from django.conf.urls import url
from django.contrib import admin
from django.contrib import admin
from project import view
from project import user_system
from project import settings
from django.views.static import serve
admin.autodiscover()
# from UserSystem import view
# from django.views.generic.simple import direct_to_template

"""
admin:heqiang password:heqiangl992
"""

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url('^hello/$', hello),
    # url("^time/(\d{1,2})/$",time_ahead),
    # url("^currenttime/$",current_datetime),
    # url("^thanks/$",thanks),
    # url("^search_page/$",view.search_page),
    # url("^search/$",view.search),
    # url("^contact/$",view.contact),
    # url(r"^about/$", direct_to_template, {
    #     'template': 'about.html'
    # }),
    # 没有调用view(direct_to_template视图仅仅是直接从传递过来的额外参数获取信息并用于渲染视图。)
    # 接受字符和数字:\w+
    url("^user_create/$", user_system.user_create),
    url("^login/$", user_system.login),
    url("^cute/$", view.home),
    url("^logout/$", user_system.logout),
    url("^userInfo/$", user_system.user_info_query),
    url("^change_userInfo/$", user_system.user_info_change),
    url("^change_passwd/$", user_system.change_password),
    url("^create_code_img/$", view.create_code_img),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATICFILES_DIRS})
]

