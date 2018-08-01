#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from log import log_info


class ContactForm(forms.Form):
    # from类先校验传入数据，
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(required=False)
    message = forms.CharField(widget=forms.Textarea)
    test = forms.CharField(required=False, label='test(rendered)')

    def clean_message(self):
        # 校验邮箱格式
        # form系统自动寻找匹配的函数方法，该方法名称以clean_开头，并以字段名称结束。 如果有这样的方法，它将在校验时被调用。
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError("Not enough words!")
        return message


class createUserForm(forms.Form):
    # 表单中的每一个字段（域）作为Form类的属性，被展现成Field类
    # input type=”text” 它应该被显示成<、、textarea、、>。我们可以通过设置* widget*来修改
    try:
        # 变量名与传入表单名字相同。
        Name = forms.CharField(widget=forms.Textarea, max_length=15)
        password = forms.CharField(widget=forms.Textarea, max_length=15)
        email = forms.CharField(widget=forms.Textarea, max_length=15, )
        safe_question = forms.CharField(widget=forms.Textarea, max_length=100, )
        answer = forms.CharField(widget=forms.Textarea, max_length=20, )
        tel = forms.CharField(widget=forms.Textarea, max_length=11, min_length=11)
        message = forms.CharField(widget=forms.Textarea, required=False, max_length=100)
    except Exception as e:
        log_info(e)


class LoginForm(forms.Form):
    username = forms.CharField(required=True, label=u"用户名", error_messages={'required': '请输入用户名'},
                               widget=forms.TextInput(attrs={'placeholder': u"用户名", }), )

    password = forms.CharField(required=True, label=u"密码", error_messages={'required': u'请输入密码'},
                               widget=forms.PasswordInput(attrs={'placeholder': u"密码", }), )

    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError(u"用户名和密码为必填项")
        else:
            cleaned_data = super(LoginForm, self).clean()
