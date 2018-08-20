#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
reload(sys)
sys.setdefaultencoding('utf8')

from django.template import Template, Context, loader
from django.shortcuts import render_to_response
from django.http import HttpResponse
import datetime
from UserSystem import models
from django.http import HttpResponseRedirect
from django.http import Http404
from django.template import TemplateDoesNotExist

from project.form import createUserForm, LoginForm
from django.contrib import auth
from django.contrib.auth.models import User
from Xml_Dir import XML
from crypt import AESCrypt
import os
from template.user_system.qustions import question
from log import log_info
import traceback


def delete_user(Name):
    itemList = User.objects.filter(Name)
    if len(itemList) > 0:
        itemList.delete()


def user_create(request):
    if request.method == 'GET':
        data = {}
        t = loader.get_template("create_user.html")
        data["ques"] = question().ques.values()
        html = t.render(data)
        return HttpResponse(html)
    if request.method == 'POST':
        form = createUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            create_user(cd)
            t = loader.get_template("create_user.html")
            html = t.render({'person_name': cd["Name"]})
            return HttpResponse(html)
        else:
            raise Http404("错误的表单")


def user_save(formDir):
    # 存入自己创的表，弃用
    db = models.user.objects
    itemList = db.filter(name=formDir["name"])
    if len(itemList) != 0:
        raise Http404()
    else:
        res = models.user(name=formDir["name"],
                          password=formDir["password"],
                          level=formDir["level"])
        res.save()
        return True


def create_user(user_info):
    user = User.objects
    db = models.user_info.objects
    itemList = user.filter(username=user_info["Name"])
    if len(itemList) != 0:
        raise Http404("用户名重复")
    else:
        try:
            authItem = user.create_user(username=user_info["Name"],
                                        email=user_info["email"],
                                        password=user_info["password"])
            user.is_staff = False
            db.create(
                user=authItem,
                safe_question=user_info["safe_question"],
                answer=user_info["answer"],
                tel=user_info["tel"],
                info=user_info["message"]
            )
            log_info(user_info["safe_question"].decode("utf-8"))
        except Exception as e:
            log_info(e, traceback.format_exc())
            delete_user(user_info["Name"])


def change_password():
    pass


def user_info_query(request):
    if request.user.is_authenticated():
        data = {}
        user = User.objects.get(username=request.user.username)
        user_info = user.user_info_set.all()[0]
        data["username"] = user.username
        data["email"] = user.email
        data["safe_question"] = user_info.safe_question
        data["tel"] = user_info.tel
        data["info"] = user_info.info
        return render_to_response('user_information.html', data)
    else:
        raise Http404("请确认是否登陆。")


def login(request):
    if request.method == 'GET':
        return render_to_response('login.html', {})
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # username = request.POST.get('username','')
            # password = request.POST.get('password','')
            user = auth.authenticate(username=cd["username"], password=cd["password"])
            if user is not None and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect("/cute/")
            else:
                return render_to_response('login.html', {'password_is_wrong': True})
        else:
            return render_to_response("login.html", {'password_is_wrong': True})
    # 全局context处理器默认情况下，Django采用参数TEMPLA1 ~TEXT_PROCESSORS指定默认处理器，
    # 意味着只要是调用的RequestContext，那么默认处理器中返回的     对象都就将存储在context中。


def logout(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/cute/")


def user_info(request):
    data = {}
    if request.user.is_authenticated():
        data["username"] = request.user.username
        t = loader.get_template("user_info.html")
        html = t.render(data)
        return HttpResponse(html)
    else:
        raise Http404("error")
