#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from log import log_info
from django.contrib.auth.models import User


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

    # 变量名与传入表单名字相同。
    username = forms.CharField(widget=forms.Textarea, min_length=6, max_length=15,
                               error_messages={"required": "不能为空", "invalid": "格式错误", "min_length": "至少6位",
                                               "max_length": "至多15位"})
    password = forms.CharField(widget=forms.Textarea, min_length=6, max_length=15,
                               error_messages={"required": "不能为空", "invalid": "格式错误", "min_length": "至少6位",
                                               "max_length": "至多15位"})
    again_password = forms.CharField(widget=forms.Textarea, min_length=6, max_length=15,
                                     error_messages={"required": "不能为空", "invalid": "格式错误", "min_length": "至少6位",
                                                     "max_length": "至多15位"})
    email = forms.CharField(widget=forms.Textarea, min_length=6, max_length=20,
                            error_messages={"required": "不能为空", "invalid": "格式错误", "min_length": "至少6位",
                                            "max_length": "至多15位"})
    safe_question = forms.CharField(widget=forms.Textarea, max_length=100, min_length=6,
                                    error_messages={"required": "不能为空", "invalid": "格式错误", "min_length": "至少6位",
                                                    "max_length": "至多100位"})
    answer = forms.CharField(widget=forms.Textarea, max_length=20, min_length=6,
                             error_messages={"required": "不能为空", "invalid": "格式错误", "min_length": "至少6位",
                                             "max_length": "至多20位"})
    tel = forms.CharField(widget=forms.Textarea, max_length=20, min_length=6,
                          error_messages={"required": "不能为空", "invalid": "格式错误", "min_length": "至少6位",
                                          "max_length": "至多20位"})
    verifycode = forms.CharField(widget=forms.Textarea, max_length=4, min_length=4,
                          error_messages={"required": "请输入验证码", "invalid": "格式错误", "min_length": "至少4位",
                                          "max_length": "至多4位"})
    info = forms.CharField(widget=forms.Textarea, required=False, max_length=100, min_length=6,
                           error_messages={"required": "不能为空", "invalid": "格式错误", "min_length": "至少6位",
                                           "max_length": "至多100位"})

    def clean(self):
        # itemList = User.objects.filter(username=self.cleaned_data["username"])
        # if len(itemList) != 0:
        #     error_msg = "用户名已被使用"
        #     self.errors["Name"] = error_msg
        password = self.cleaned_data["password"]
        again_password = self.cleaned_data["again_password"]
        if password != again_password:
            error_msg = "密码不一致"
            self.errors["password"] = error_msg
        return self.cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(required=True, label=u"用户名", error_messages={'required': '请输入用户名'},
                               widget=forms.TextInput(attrs={'placeholder': u"用户名", }), max_length=12)

    password = forms.CharField(required=True, label=u"密码", error_messages={'required': u'请输入密码'},
                               widget=forms.PasswordInput(attrs={'placeholder': u"密码", }), max_length=15)

    verifycode = forms.CharField(required=True, label=u"验证码", error_messages={'required': '请输入验证码'},
                                 widget=forms.TextInput(attrs={'placeholder': u"验证码", }), max_length=4)


class change_userinfo_form(forms.Form):
    tel = forms.IntegerField(widget=forms.Textarea, max_value=11, min_value=8,
                             error_messages={"required": "不能为空", "invalid": "格式错误", "min_length": "至少8位",
                                             "max_length": "至多11位"})
    info = forms.CharField(widget=forms.Textarea, required=False, max_length=100, min_length=6,
                           error_messages={"required": "不能为空", "invalid": "格式错误", "min_length": "至少6位",
                                           "max_length": "至多100位"})


class change_password_form(forms.Form):
    old_password = forms.CharField(widget=forms.Textarea, min_length=6, max_length=15,
                                   error_messages={"required": "不能为空", "invalid": "格式错误", "min_length": "至少6位",
                                                   "max_length": "至多15位"})
    new_password = forms.CharField(widget=forms.Textarea, min_length=6, max_length=15,
                                   error_messages={"required": "不能为空", "invalid": "格式错误", "min_length": "至少6位",
                                                   "max_length": "至多15位"})
    again_password = forms.CharField(widget=forms.Textarea, min_length=6, max_length=15,
                                     error_messages={"required": "不能为空", "invalid": "格式错误", "min_length": "至少6位",
                                                     "max_length": "至多15位"})

    def clean(self):
        new_password = self.changed_data["password"]
        again_password = self.cleaned_data["again_password"]
        if new_password != again_password:
            error_msg = "密码不一致"
            self.errors["new_password"] = error_msg
        return self.cleaned_data
