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
from project.form import createUserForm
from UserSystem import models
from log import logger

def user_create(request):

    if request.method == 'GET':
        t = loader.get_template("create_user.html")
        html = t.render({'person_name': "", 'authors': "", 'query': ""})
        return HttpResponse(html)
    if request.method == 'POST':
        form = createUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user_save(cd)
        t = loader.get_template("create_user.html")
        html = t.render({'person_name': cd["name"], 'authors': "", 'query': ""})
        return HttpResponse(html)

def about_pages(request, page):
    pass
    # try:
    #     return direct_to_template(request, template="about/%s.html" % page)
    # except TemplateDoesNotExist:
    #     raise Http404()

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
        logger.info(res.id)
        return True
