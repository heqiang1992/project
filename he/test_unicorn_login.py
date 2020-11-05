#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author:heqiang

import time
from lib.SSHRemoteOperation import log
from lib.NodesConfigurations import Configurations
from common.HyhiveCommon.HyhiveRestAPI.HyhiveUser import HyhiveUser
from common.HyhiveCommon import TestConf
import requests, json, re
import execjs


class test_unicorn_login:
    def pre_condiction(self):
        log.logger.info("预置步骤1:HyHive平台服务正常")
        bed = Configurations()
        global nodes, user, user_name, password
        nodes = bed.allnodelist
        user_name = TestConf.USER_ONE_NAME
        password = TestConf.USER_ONE_PWD

    def product(self):

        url1 = "http://10.0.40.227:9535/auth/realms/default/protocol/openid-connect/auth?client_id=unicorn-admin-console&" \
               "redirect_uri=http%3A%2F%2F10.0.40.227%3A3000%2F%23%2Flaunchpad%3F&state=0d0f59fd-ee3e-4522-802f-87b6b35bf416&" \
               "response_mode=fragment&response_type=code&scope=openid&nonce=9a7fd464-07bf-4912-87d5-5a2f5db2f579&" \
               "code_challenge=GEG4WotqTAVX7wRoFhHhJNe9_pNbhPMI0J8VXndIAIw&code_challenge_method=S256"
        con = requests.get(url=url1)
        content = con.content.decode("utf-8")
        # print(content)
        url = re.search("http://\d.+tab_id=\w+", content).group(0)
        # url = re.search("client_id=.+&", content).group(0)
        change_url = url.replace("&amp;", "&")
        # header = con.headers
        cookie = con.cookies
        print(change_url)
        data = {"username": "admin", "password": "123456"}

        header = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Length": "31",
            "Content-Type": "application/x-www-form-urlencoded",
            "Host": "10.0.40.227:9535",
            "Origin": "http://10.0.40.227:9535",
            "Pragma": "no-cache",
            "Referer": url1,
            "Upgrade-Insecure-Requests": "1"
        }
        con = requests.post(url=change_url, data=data, headers=header, cookies=cookie)
        # content = con.content.decode("utf-8")
        cookies_200 = con.cookies  # 后面用
        responce_302 = con.history[0]
        print(responce_302.status_code)
        # header = con.headers
        cookie = responce_302.cookies
        # print(content)
        location = responce_302.headers.get("location")
        datacode = location.split("code=")[-1]
        data = {"code": datacode,
                "grant_type": "authorization_code",
                "client_id": "unicorn-admin-console",
                "redirect_uri": "http://10.0.40.227:3000/#/launchpad?",
                "code_verifier": "ZkzaVPelmoX8e1FSK4ahhqjl224uqXf6SvIk7pGSE98"
                }
        header = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Length": "352",
            "Content-Type": "application/x-www-form-urlencoded",
            "Host": "10.0.40.227:9535",
            "Origin": "http://10.0.40.227:3000",
            "Pragma": "no-cache",
            "Referer": "http://10.0.40.227:3000/"
        }
        con_token = requests.post("http://10.0.40.227:9535/auth/realms/default/protocol/openid-connect/token",
                                  data=data, headers=header, cookies=cookie)
        assert con_token.status_code == 200
        content = con_token.content.decode("utf-8")
        content_dir = json.loads(content)
        token_cookie = con_token.cookies
        access_token = "Bearer " + content_dir["access_token"]
        cookies_200_dict = requests.utils.dict_from_cookiejar(cookies_200)
        cookies_200_dict["access_token"] = access_token
        import http.cookiejar as cookiejar
        cj = cookiejar.CookieJar()
        user_cookies = requests.utils.add_dict_to_cookiejar(cj=cj, cookie_dict=cookies_200_dict)

        # f = open("D:\\unicorn.csv", mode="r")
        # f.seek(0, 0)
        # file_lines = f.readlines()
        # f2 = open("d:\\userinfo.csv", mode="a+")
        for i in range(100):
            user = "user%s" % str(i)
            data = {"realm": "test", "username": user, "groups": ["/group001"], "attributes": {},
                    "enabled": True,
                    "emailVerified": False,
                    "credentials": [{"value": "123456"}]
                    }

            url = "http://10.0.40.227:3000/auth/tenant/user/create"
            header = {
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "zh-CN,zh;q=0.9",
                "Access-Control-Allow-Origin": "*",
                "access-token": access_token,
                "Cache-Control": "no-cache",
                "Connection": "keep-alive",
                "Content-Length": "111",
                "Content-Type": "application/json",
                "Host": "10.0.40.227:3000",
                "Origin": "http://10.0.40.227:3000",
                "Pragma": "no-cache",
                "Referer": "http://10.0.40.227:3000/"
            }
            c = requests.post(url=url, data=json.dumps(data), headers=header, cookies=user_cookies)
            print(c.status_code)
            # codes = file_lines[i].strip("\r\n")
            # if codes.endswith(","):
            #     line = codes + user + "\r"
            #     f2.write(line)
        #
        # f.close()
        # f2.close()


    def post_condiction(self):
        pass
