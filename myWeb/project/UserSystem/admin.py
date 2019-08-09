# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
"""
admin：heqiang
password:heqiang1992
"""
from .models import user_info, case, case_report


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')
    list_filter = ('last_name',)
    # filter_horizontal = ('last_name',)


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date')
    list_filter = ('publication_date',)
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)
    fields = ('title', 'authors', 'publisher', 'publication_date')


admin.site.register(user_info)
admin.site.register(case)
admin.site.register(case_report)
