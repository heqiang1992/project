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
from django.conf.urls import url
from django.contrib import admin
from project.view import hello,time_ahead,current_datetime,thanks
from django.contrib import admin
from project import view
admin.autodiscover()




urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^hello/$', hello),
    url("^time/(\d{1,2})/$",time_ahead),
    url("^currenttime/$",current_datetime),
    url("^thanks/$",thanks),
    url("^search_page/$",view.search_page),
    url("^search/$",view.search),
    url("^contact/$",view.contact),
]
