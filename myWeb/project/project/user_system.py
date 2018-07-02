#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.template import Template, Context,loader
from django.shortcuts import render_to_response
from django.http import HttpResponse
import datetime
import time
from UserSystem import models
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.http import Http404
from django.template import TemplateDoesNotExist
from UserSystem import models
from project.form import createUserForm,LoginForm
from django.contrib import auth
from django.template.context import RequestContext
from django.contrib.auth.models import User

def user_create(request):
    if request.method == 'GET':
        t = loader.get_template("create_user.html")
        html = t.render({'person_name': "", 'authors': "", 'query': ""})
        return HttpResponse(html)
    if request.method == 'POST':
        form = createUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned一data
            user_save(cd)
            t = loader.get_template("create_user.html")
            html = t.render({'person_name': cd["Name"], 'authors': "", 'query': ""})
            return HttpResponse(html)
        else:
            raise Http404("错误的表单")



def user_save(formDir):
    db = models.user.objects
    itemList = db.filter(name=formDir["name"])
    if len(itemList) != 0:
        raise Http404()
    else:
        res = models.user(name=formDir["name"],
                    password=formDir["password"],
                    level=formDir["level"]
                    )
        res.save()
        return True

def user_demo(request):
    if request.user.is_authenticated():
        pass
        # Do something for authenticated users. pass
    else:
        pass
        # Do something for anonymous users• pass

def login(request):
    if request.method == 'GET':
        return render_to_response('login.html', {})
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned一data
            # username = request.POST.get('username','')
            # password = request.POST.get('password','')
            user = auth.authenticate(username=cd["username"], password=cd["password"])
            if user is not None and user.is_active:
                auth.login(request, user)
                return render_to_response('search_form.html',{})
            else:
                return render_to_response('login.html',{'password_is_wrong':True})
        else:
            return render_to_response("login.html", RequestContext(request, {'form': "",}))
    #全局context处理器默认情况下，Django采用参数TEMPLA1 ~TEXT_PROCESSORS指定默认处理器，
    #意味着只要是调用的RequestContext，那么默认处理器中返回的     对象都就将存储在context中。

def logout_view(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/account/loggedout/")
