#-*- coding:utf-8 -*-
__autthor__="heqiang"

import xml
from xml.dom.minidom import parse
import xml.dom.minidom

class XML():
    def __init__(self,xmlPath):
        self.__counter = 0
        self.XML =xml.dom.minidom.parse(xmlPath).documentElement
        self.dir = {}
        self.__analysis(self.XML)

    def __read_device(self):
        device = self.XML.getElementsByTagName("device")[0]
        print(dir(device.childNodes))

    def __analysis(self,root):

        for i in  root.childNodes:
            if hasattr(i,"tagName") and i.childNodes > 1:
                self.__analysis(i)
            elif len(i.childNodes) == 0 :
                attrib= {}
                for attributeName in i.parentNode._attrsNS.keys():
                    attributeNameDraw =[k for k in attributeName if k not in [""," ",None]]
                    if len(attributeNameDraw) != 0:
                        valueName = "".join(attributeNameDraw)
                        attrib[valueName]=i.parentNode._attrsNS[attributeName].value
                parentNode = i.parentNode.parentNode.localName
                node={}
                node["parentNode"]=parentNode
                node["__nodelevel"]=self.__nodelevel(i.parentNode)
                node["data"]=i.data
                node["attribute"]=attrib
                self.__counter=0
                self.dir[i.parentNode.tagName] = node
            else:
                pass

    def __nodelevel(self,node):
        if node.parentNode != None:
            self.__nodelevel(node.parentNode)
            self.__counter +=1
        level = self.__counter
        return level


if (__name__=="__main__"):
    i = XML("")

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
