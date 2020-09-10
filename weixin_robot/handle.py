#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author:heqiang

from flask import Flask, request, make_response
import hashlib
import re
import xml.dom.minidom
import weixin_robot.aetaoke as aetaoke
import xmltodict
from weixin_robot import model
import datetime


def handle_rec(content):
    """
    <xml><ToUserName><![CDATA[gh_9916f0d0036e]]></ToUserName>
    <FromUserName><![CDATA[oYzyEv5y_PWiC3_8BuaH90Lw-BMk]]></FromUserName>
    <CreateTime>1596771619</CreateTime>
    <MsgType><![CDATA[text]]></MsgType>
    <Content><![CDATA[89]]></Content>
    <MsgId>22860274477589510</MsgId>
    </xml>
    :param content:
    :return:
    """
    server_tag = re.search("<ToUserName>.+</ToUserName>", content).group(0)
    user_tag = re.search("<FromUserName>.+</FromUserName>", content).group(0)
    server_tag = server_tag.replace("ToUserName", "FromUserName")
    user_tag = user_tag.replace("FromUserName", "ToUserName")
    n1 = re.sub("<ToUserName>.+</ToUserName>", user_tag, content)
    n2 = re.sub("<FromUserName>.+</FromUserName>", server_tag, n1)
    return n2


def parse_msg(rec):
    """

    :param rec:
    :return:
    """

    rec_gbk = rec.decode("utf-8")

    if re.search("<Content>", rec_gbk):
        xml_tool = xml.dom.minidom.Document()
        msg_tree = xml.dom.minidom.parseString(rec_gbk).documentElement
        content = msg_tree.getElementsByTagName("Content")[0]
        FromUserName = msg_tree.getElementsByTagName("FromUserName")[0]
        message = content.firstChild.data
        weixinID = FromUserName.firstChild.data
        if re.search("\w{11}", message):
            bool_flag, juan_tkl, tao_id = aetaoke.tkl_api(message)
            # 计录券
            if bool_flag:
                now_time = datetime.datetime.now()
                now_time = now_time.strftime('%Y-%m-%d %H:%M:%S')
                model.add_tkl_record(username=weixinID, re_time=now_time, tkl=juan_tkl, tao_id=tao_id)
                # 检查用户
                check_user = model.check_user(username=weixinID)
                if check_user is None:
                    model.add_user(username=weixinID)
        elif re.search("^查询", message):
            pass
        elif re.search("^提现", message):
            pass
        elif re.search("^提现", message):
            pass
        else:
            juan_tkl = "不支持的其他类型信息"
        text = xml_tool.createTextNode(juan_tkl)
        content.removeChild(content.firstChild)
        content.appendChild(text)
        xml_str = msg_tree.toprettyxml()
        message_str = xml_str.replace("\n", "").replace("\t", "")
        response_message = handle_rec(message_str)
        return response_message.encode("utf-8")
    else:
        pass


def settle_accounts(month):
    """
    结算上个月的已结算订单
    month : int
    :return:
    """


if __name__ == "__main__":
    a = b"<xml><ToUserName><![CDATA[gh_9916f0d0036e]]></ToUserName>\
<FromUserName><![CDATA[oYzyEv5y_PWiC3_8BuaH90Lw-BMk]]></FromUserName>\
<CreateTime>1596771619</CreateTime>\
<MsgType><![CDATA[text]]></MsgType>\
<Content><![CDATA[89123456789]]></Content>\
<MsgId>22860274477589510</MsgId>\
</xml>"
    parse_msg(a)
