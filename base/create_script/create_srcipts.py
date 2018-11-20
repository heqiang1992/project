#!/usr/bin/python
# -*- coding: utf-8 -*-

import xlrd,re


class create_auto():

    def __init__(self):
        self.sheet=self.read_excel("d")
        self.start_create()

    def read_excel(self,file_path,index=0):
        data = xlrd.open_workbook("d:\\book1.xls")
        sheet = data.sheets()[index]
        return sheet

    def write(self,cmd):
        CMD=cmd.upper()
        name=re.sub(" ","_",CMD)
        ID=re.sub(" ",".",CMD)
        py_name="d:\\"+name+".py"


        file=open(py_name,"a+")
        file.write("    \t,\n   哦 ")
        file.write(name)
        file.write("    \t,\n   sss ")
        file.write(ID)
        file.write("    \t,\n  好  ")
        file.write(cmd)
        file.write("")
        file.close()


    def start_create(self):
        for rownum in range(0,self.sheet.nrows):
            row = self.sheet.row_values(rownum)
            self.write(row[0])

a=create_auto()