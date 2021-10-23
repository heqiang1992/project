# -*- coding:utf-8 -*-
__autthor__ = "heqiang"

import xml
from xml.dom.minidom import parse
import xml.dom.minidom
import os, re


# python
class XML(object):
    def __init__(self, xmlPath):
        self.__counter = 0
        self.XML = xml.dom.minidom.parse(xmlPath).documentElement
        self.dir = {}
        self.__analysis(self.XML)

    def __read_device(self):
        device = self.XML.getElementsByTagName("device")[0]
        print(dir(device.childNodes))

    def __analysis(self, root):

        for i in root.childNodes:
            if hasattr(i, "tagName") and i.childNodes > 1:
                self.__analysis(i)
            elif len(i.childNodes) == 0:
                attrib = {}
                for attributeName in i.parentNode._attrsNS.keys():
                    attributeNameDraw = [k for k in attributeName if k not in ["", " ", None]]
                    if len(attributeNameDraw) != 0:
                        valueName = "".join(attributeNameDraw)
                        attrib[valueName] = i.parentNode._attrsNS[attributeName].value
                parentNode = i.parentNode.parentNode.localName
                node = {}
                node["parentNode"] = parentNode
                node["__nodelevel"] = self.__nodelevel(i.parentNode)
                node["data"] = i.data
                node["attribute"] = attrib
                self.__counter = 0
                # 在这一步解决重名问题
                if self.dir.has_key(i.parentNode.tagName):
                    if isinstance(self.dir[i.parentNode.tagName], list):
                        self.dir[i.parentNode.tagName].append(node)
                    else:
                        values_ex = [self.dir[i.parentNode.tagName], node]
                        self.dir[i.parentNode.tagName] = values_ex
                else:
                    self.dir[i.parentNode.tagName] = node
            else:
                pass

    def __nodelevel(self, node):
        if node.parentNode != None:
            self.__nodelevel(node.parentNode)
            self.__counter += 1
        level = self.__counter
        return level


# if (__name__ == "__main__"):
#     i = XML("")

"""
生成dom对象
import xml.dom.minidom
domdoc = xml.dom.minidom.parse("path")
获取元素对象
root=domdoc.documentElement
元素属性
root.nodeName[元素名]
root.nodeType[元素类型]
root.nodeValue[元素值]
子元素的访问
root.getElementsByTagName("")
root.childNodes
"""

case_template = """<id id="%s" run="%s" tag="%s">
        <case_id>%s</case_id>
        <case_name>%s</case_name>
        <case_path>%s</case_path>
    </id>"""


def write_template(file):
    string = """<?xml version='1.0' encoding='utf-8'?>
    <foo>
    <parameter paralle = "0" order = "1" timeout = "0" reptype = "long">
    </parameter>
    """
    file.write(string)



def xml_write(file, filePath):
    # 将文件信息填入格式中，写入
    "D:\code\auto-test\testCase\hyhive_testCase\HyhiveV2\project_manage\test_6545_UserLogin_DisabledProject.py"
    # print(filePath)
    id_demo = re.search("_\d{4,5}_", filePath).group(0)
    id = id_demo.replace("_", "")
    case_file = re.search("\\w+\.py", filePath).group(0)
    case_name = case_file.replace("\\", "").replace(".py", "")
    opposite_path = "testCase" + filePath.split("\\testCase")[-1]
    c = case_template % (id, "1", "1", case_name, case_name, opposite_path)
    file.write("\n")
    file.write(c)


def demo(file, root_dir):
    # 收集目录下的py文件生成xml格式用例集写入文件

    search_items = os.listdir(root_dir)
    for sub in search_items:
        s = os.path.join(root_dir, sub)
        if os.path.isdir(s):
            demo(file=file, root_dir=s)
        elif re.search("test_.+\.py$", s):
            # 生成xml格式写入文件
            xml_write(file, s)


f = open(r"D:\code\sc\project_manage.xml", mode="w+")
write_template(f)
demo(file=f, root_dir="D:\\code\\auto-test\\testCase\\hyhive_testCase\\HyhiveV2\\project_manage\\")
f.write("\n</foo>")
f.close()

f = open(r"D:\code\sc\image_manage.xml", mode="w+")
write_template(f)
demo(file=f, root_dir="D:\\code\\auto-test\\testCase\\hyhive_testCase\\HyhiveV2\\image_manage\\")
f.write("\n</foo>")
f.close()

f = open(r"D:\code\sc\cinder_manage.xml", mode="w+")
write_template(f)
demo(file=f, root_dir="D:\\code\\auto-test\\testCase\\hyhive_testCase\\HyhiveV2\\cinder_manage\\")
f.write("\n</foo>")
f.close()

f = open(r"D:\code\sc\resource_manage.xml", mode="w+")
write_template(f)
demo(file=f, root_dir="D:\\code\\auto-test\\testCase\\hyhive_testCase\\HyhiveV2\\resource_manage\\")
f.write("\n</foo>")
f.close()
