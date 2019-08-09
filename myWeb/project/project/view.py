#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.template import Template, Context, loader
from django.shortcuts import render_to_response
from django.http import HttpResponse
import datetime
from io import BytesIO
from .random_checkcode import Captcha
import time
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from project.form_usersys import ContactForm
from django.http import Http404
from django.template import TemplateDoesNotExist


# from django.views.generic.simple import direct_to_template


def home(request):
    now_time = datetime.datetime.now()
    date = now_time.strftime('%Y-%m-%d %H:%M:%S')

    t = loader.get_template("cute.html")
    data = {"now_time": date}
    if request.user.is_authenticated:
        data["username"] = request.user.username
    html = t.render(data)
    return HttpResponse(html)


def create_code_img(request):
    f = BytesIO()  # 直接在内存开辟一点空间存放临时生成的图片

    code, img = Captcha.gene_code()  # 调用check_code生成照片和验证码
    request.session['check_code'] = code  # 将验证码存在服务器的session中，用于校验
    img.save(f, 'png')  # 生成的图片放置于开辟的内存中
    return HttpResponse(f.getvalue())  # 将内存的数据读取出来，并以HttpResponse返回


"""

def hello(request):
    Dtime=datetime.datetime.now()
    Dtime= Dtime.strftime('%b-%d-%Y %H:%M:%S')

    content="<html>" \
            "<body>Hello world         im here     \n  %s</body>" \
            "</html>"%Dtime
    return HttpResponse(content)


def time_ahead(request,offset):

    timestamp = time.time()
    try:
        offset = int(offset)
    except TypeError:
        raise ("请求的小时数不对")
    timestamp += offset*3600

    Time= datetime.datetime.fromtimestamp(timestamp)

    content="<html>" \
            "<body>Hello world         im here     \n  in %s hours, time is %s</body>" \
            "</html>"%(offset,Time)
    return HttpResponse(content)


def current_datetime(request):
    now = datetime.datetime.now()
    t = Template("<html><body>It is now {{ current_date }}.</body></html>")
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)

def thanks(request):
    now_time = datetime.datetime.now()
    date = now_time.strftime('%Y-%m-%d %H:%M:%S')[:10]
    # f=open("D:\component\Django\project\project\\template\\thankmail.html","a+")
    # t = Template(f.read())
    # f.close()
    t = loader.get_template("thankmail.html")
    #教程中老板本使用context传入loader.get_templat，在新版Django中会报错。解决办法：不处理，直接传入字典。
    # html = t.render(Context(
    #     {'ship_date': date,"person_name":"heqiang","company":"Tencent",
    #      "item_list":["power","monney","women"],}
    # ))
    html = t.render(
        {'ship_date': date,"person_name":"heqiang","company":"Tencent",
         "item_list":["power","monney","women"]}
    )
    return HttpResponse(html)

def search_page(request):
    #废弃
    now_time = datetime.datetime.now()
    date = now_time.strftime('%Y-%m-%d %H:%M:%S')[:10]

    t = loader.get_template("search_form.html")

    user_addr=request.META["REMOTE_ADDR"]
    html = t.render(
        {"person_name":user_addr}
    )
    return HttpResponse(html)

def search(request):
    error = False
    user_addr = request.META["REMOTE_ADDR"]
    if 'q' in request.GET:

        q=request.GET['q']
        authors = models.Author.objects.filter(last_name__icontains=q)
        t=loader.get_template("search_form.html")
        html = t.render({'person_name':user_addr,'authors': authors,'query': q})
        return HttpResponse(html)
    else:
        error=True
        return render_to_response('search_form.html', {'person_name':user_addr,'error':error})

def contact(request):

    # errors = []
    # if request.method == 'POST':
    #     if not request.POST.get('subject', ''):
    #         errors.append('Enter a subject.')
    #     if not request.POST.get('message', ''):
    #         errors.append('Enter a message.')
    #     if not request.POST.get('email') or '@' not in request.POST['email']:
    #         errors.append('Enter a valid e-mail address.')
    #     if not errors:
    #         #可自己实现send
    #         send_mail(
    #             request.POST['subject'],
    #             request.POST['message'],
    #             request.POST.get('email', 'noreply@example.com'),
    #             ['siteowner@example.com'],
    #         )
    #         #
    #         return HttpResponseRedirect('/thanks/')
    # return render_to_response('contact_form.html',
    #     {'errors': errors})
    # 运用form类重写。


    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/thanks/')
    else:
        form = ContactForm(initial={'subject': 'I love your site!'})
    return render_to_response('contact_form.html', {'form': form})


@可直接使用render_to_response简化整个流程
from django.shortcuts import render_to_response
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('current_datetime.html', {'current_date': now})

读取cookies
request.COOKIES

@写cookies 
response=HttpResponse(html) 
response.set_cookie("favorite_color"，request.GET["favorite_color"])


@在视图中使用Session
# Set a session value: 
request.session["fav_color"] = "blue"
# Get a session value -- this could be called in a diff erent view,
# or many requests later (or both): 
fav_color = request.session["fav_color"] 
# Clear an item from the session:
del request.session["fav_color"]
# Check if the session has a given key: 
if "fav_color" in request.session:

"""
