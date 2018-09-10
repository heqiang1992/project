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

from project.form_usersys import createUserForm, LoginForm, change_password_form, change_userinfo_form
from django.contrib import auth
from django.contrib.auth.models import User
from random_checkcode import Captcha
from crypt import AESCrypt
from template.user_system.qustions import question
from log import log_info
import traceback


def delete_user(Name):
    itemList = User.objects.filter(Name)
    if len(itemList) > 0:
        itemList.delete()


def user_create(request):
    data = {}
    if request.method == 'GET':
        data["ques"] = question().ques.values()
        t = loader.get_template("create_user.html")
        html = t.render(data)
        return HttpResponse(html)
    if request.method == 'POST':
        form = createUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd["verifycode"].lower() == request.session['check_code'].lower():
                create_user(cd)
                t = loader.get_template("create_user.html")
                html = t.render({'person_name': cd["username"]})
                return HttpResponse(html)
            else:
                data["ques"] = question().ques.values()
                data["verify_error"] = "验证码错误"
                t = loader.get_template("create_user.html")
                html = t.render(data)
                return HttpResponse(html)
        else:
            data["ques"] = question().ques.values()
            data["form"] = form
            return render_to_response("create_user.html", data)


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
    itemList = user.filter(username=user_info["username"])
    if len(itemList) != 0:
        raise Http404("用户名重复")
    else:
        try:
            authItem = user.create_user(username=user_info["username"],
                                        email=user_info["email"],
                                        password=user_info["password"])
            user.is_staff = False
            db.create(
                user=authItem,
                safe_question=user_info["safe_question"],
                answer=user_info["answer"],
                tel=user_info["tel"],
                info=user_info["info"]
            )

        except Exception as e:
            log_info(e, traceback.format_exc())
            delete_user(user_info["username"])


def change_password(request):
    data = {}
    if request.user.is_authenticated():
        if request.method == 'GET':
            return render_to_response("change_password.html", {})

        elif request.method == 'POST':
            form = change_password_form(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                login_user = auth.authenticate(usemame=request.user.usemame, password=cd["old_password"])
                if login_user is not None and login_user.is_active:
                    login_user.set_password(cd["new_password"])
                    login_user.save()
                else:
                    data["auth_error"] = "原密码验证失败"
                    return render_to_response("change_password.html", data)
            else:
                data["form"] = form
                return render_to_response("change_password.html", data)
    else:
        data["auth_error"] = "请确认用户是否登录"
        return render_to_response("change_password.html", data)


def user_info_query(request):
    data = {}
    if request.user.is_authenticated():

        user = User.objects.get(username=request.user.username)
        user_info = user.user_info_set.all()[0]
        data["username"] = user.username
        data["email"] = user.email
        data["safe_question"] = user_info.safe_question
        data["tel"] = user_info.tel
        data["info"] = user_info.info
        return render_to_response('user_information.html', data)
    else:
        data["auth_error"] = "请确认是否登录"
        return render_to_response("user_infomation.html", data)


def user_info_change(request):
    data = {}
    if request.user.is_authenticated():
        data["change_info"] = True
        if request.method == 'GET':
            return render_to_response("user_information.html", data)
    elif request.method == "POST":
        user = User.objects.get(usemame=request.user.usemame)
        user_info = user.user_info_set.all()
        form = change_userinfo_form(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            for index, key in enumerate(["tel", "info"]):
                if cd[key] == "":
                    cd[key] = getattr(user_info[0], key)
            user_info.update(tel=cd["tel"], info=cd["info"])

            return HttpResponseRedirect("/cute/")
        else:
            data["form"] = form
            return render_to_response("user_information.html", data)
    else:
        data["auth_error"] = "请确认用户是否登录"
        return render_to_response("user_information.html", data)


def login(request):
    data = {}
    if request.method == 'GET':
        return render_to_response('login.html', {})
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd["verifycode"].lower() == request.session['check_code'].lower():
                user = auth.authenticate(username=cd["username"], password=cd["password"])
                if user is not None and user.is_active:
                    auth.login(request, user)
                    return HttpResponseRedirect("/cute/")
                else:
                    data["auth_error"] = "用户名或密码错误"
                    return render_to_response('login.html', data)
            else:
                data["verify_error"] = "验证码错误"
                return render_to_response('login.html', data)
        else:
            data["auth_error"] = "用户名或密码错误"
            return render_to_response("login.html", data)
    # 全局context处理器默认情况下，Django采用参数TEMPLA1 ~TEXT_PROCESSORS指定默认处理器，
    # 意味着只要是调用的RequestContext，那么默认处理器中返回的     对象都就将存储在context中。


def logout(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/cute/")
