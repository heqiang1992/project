#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
统计目录下的每个py文件的函数信息
"""

import os, re
import xlwt, xlrd

search_dir = r"D:\code\auto-test\common\HyhiveCommon\HyhiveRestAPI"
files = []


def list_file(dir):
    sub_list = os.listdir(dir)
    for sub in sub_list:
        s = os.path.join(dir, sub)
        if os.path.isdir(s):
            list_file(s)
        elif sub.endswith(".py") and re.search("^Hyhive", sub, re.I):
            files.append(s)


def generate_excel(files):
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet_file = workbook.add_sheet('file')
    style = xlwt.XFStyle()  # 初始化样式
    font = xlwt.Font()  # 为样式创建字体
    font.name = 'Times New Roman'
    font.bold = True  # 黑体
    font.height = 250
    style.font = font  # 设定样式

    style2 = xlwt.XFStyle()  # 初始化样式
    font = xlwt.Font()  # 为样式创建字体
    font.name = 'Times New Roman'
    font.height = 250
    style2.alignment.wrap = 1  # 自动换行
    style2.font = font  # 设定样式

    style3 = xlwt.XFStyle()  # 初始化样式
    font = xlwt.Font()  # 为样式创建字体
    font.name = 'Times New Roman'
    font.height = 250
    font.colour_index = 2
    style3.alignment.wrap = 1  # 自动换行
    style3.font = font  # 设定样式

    def getline(the_file_path, line_number):
        if line_number < 1:
            return ''
        for cur_line_number, line in enumerate(open(the_file_path, 'r+', encoding="utf-8")):
            if cur_line_number == line_number - 1:
                return line
        return ''

    def sheet_aw_write(f):
        sheetname = f.split(os.sep)[-1]
        sheetname = sheetname.replace(".py", "")
        worksheet = workbook.add_sheet(sheetname)
        for ind, tag in enumerate(["类", "函数", "参数", "注释", "备注"]):
            worksheet.write(0, ind, tag, style)
            worksheet.col(ind).width = 10000

        t = open(f, "r+", encoding="utf-8")
        classitem = re.compile("class \w+\(.*\):", re.I)
        functionitem = re.compile("def \w+\(.*\):", re.I)
        row = 1
        for i, line in enumerate(t.readlines()):  # 处理类
            if re.search(classitem, line):
                classname = re.search("class \w+\(", line).group(0)
                classname = classname.replace("class ", "").strip("(")
                worksheet.write(row, 0, classname, style)
                row += 1
            elif re.search(functionitem, line):  # 处理函数
                funcname = re.search("def \w+\(", line).group(0)
                funcname = funcname.replace("def ", "").strip("(")
                param = re.search("\(.*\)", line).group(0)
                param = param.replace("self", "").strip("(").strip(")")
                param = re.sub("^,", "", param)
                worksheet.write(row, 1, funcname, style2)
                worksheet.write(row, 2, param, style2)
                # 抓注释
                the_line = getline(f, i + 2)
                if re.search("\"\"\"", the_line):
                    annotation = ""
                    for annot in range(3, 10):
                        behind = getline(f, i + annot)
                        if re.search("\"\"\"", behind):
                            break
                        else:
                            annotation += behind
                    worksheet.write(row, 3, annotation, style2)
                else:
                    annotation = "无"
                    worksheet.write(row, 3, annotation, style3)
                row += 1

    # sheet
    for ind, file in enumerate(files):
        worksheet_file.write(ind, 0, file, style)
        sheet_aw_write(file)

    worksheet_file.col(0).width = 30000
    workbook.save('Excel_test.xls')


if __name__ == "__main__":
    list_file(dir=search_dir)
    print(files)
    generate_excel(files)
