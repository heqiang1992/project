# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.


class weibo_comment(models.Model):
    Name = models.CharField(max_length=100)
    comment_type = models.CharField(max_length=100)
    article_relation = models.CharField(max_length=100)
    comment_area = models.CharField(max_length=800)
    publication_date = models.DateField(blank=True)


class weibo_article(models.Model):

    Name = models.CharField(max_length=100)
    article_type = models.CharField(max_length=100)
    article_relation = models.CharField(max_length=100)
    article_area = models.CharField(max_length=800)
