#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author:heqiang

from flask import Flask, request, make_response
import hashlib
import re
import xml.dom.minidom
import weixin_robot.aetaoke as aetaoke
import xmltodict


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
    try:
        rec_gbk = rec.decode("gbk")
    except:
        pass
    else:
        if re.search("<Content>", rec_gbk):
            xml_tool = xml.dom.minidom.Document()
            msg_tree = xml.dom.minidom.parseString(rec_gbk).documentElement
            content = msg_tree.getElementsByTagName("Content")[0]
            message = content.firstChild.data
            juan_tkl = aetaoke.tkl_api(message)
            text = xml_tool.createTextNode(juan_tkl)
            content.removeChild(content.firstChild)
            content.appendChild(text)
            xml_str = msg_tree.toprettyxml()
            message_str = xml_str.replace("\n","").replace("\t","")
            response_message = handle_rec(message_str)
            return response_message.encode("gbk")



if __name__ == "__main__":
    a = b"<xml><ToUserName><![CDATA[gh_9916f0d0036e]]></ToUserName>\
<FromUserName><![CDATA[oYzyEv5y_PWiC3_8BuaH90Lw-BMk]]></FromUserName>\
<CreateTime>1596771619</CreateTime>\
<MsgType><![CDATA[text]]></MsgType>\
<Content><![CDATA[89]]></Content>\
<MsgId>22860274477589510</MsgId>\
</xml>"
    parse_msg(a)
