#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
统计目录下的每个py文件的函数信息
"""

import os, re
import xlwt, xlrd

# search_dir = r"D:\code\auto-test\common\HyhiveCommon\HyhiveRestAPI"
search_dir = r"D:\code\auto-test\testCase\hyhive_testCase"
files = []
old = [2526, 2527, 2523, 2524, 2522, 2528, 2528, 2556, 4472, 4473, 2514, 2515, 2516, 2518, 2520, 2540, 2541, 2546, 4714,
       4546, 2549, 4713, 2545, 2945, 2552, 2552, 2552, 4312, 3365, 2582, 2580, 2578, 4470, 2517, 3068, 2587, 2587, 2536,
       2537, 2538, 2555, 2561, 2532, 2533, 2534, 2937, 2935, 2594, 2590, 2591, 2592, 2593, 2570, 2519, 2557, 4205, 4211,
       2557, 2596, 2687, 2690, 2692, 2689, 2690, 2692, 2687, 2689, 2688, 2691, 3068, 3050, 3051, 3062, 3052, 3058, 4564,
       4567, 2534, 3054, 3055, 3063, 3062, 3064, 3069, 2703, 2965, 2967, 2714, 2715, 4513, 2538, 2985, 2555, 2988, 3018,
       2995, 2995, 3001, 3002, 3005, 3005, 3005, 3004, 2676, 2682, 3332, 3133, 3134, 3135, 3137, 3138, 3139, 3141, 3142,
       2631, 2874, 2696, 3194, 2724, 4496, 4512, 2695, 3166, 2702]


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
    # al = xlwt.Alignment()
    # al.horz = 0x02  # 设置水平居中
    # al.vert = 0x01  # 设置垂直居中
    # style.alignment = al
    style.font = font  # 设定样式

    style2 = xlwt.XFStyle()  # 初始化样式
    font = xlwt.Font()  # 为样式创建字体
    font.name = 'Times New Roman'
    font.height = 250
    al = xlwt.Alignment()
    # al.horz = 0x02  # 设置水平居中
    # al.vert = 0x01  # 设置垂直居中
    # al.wrap =1 # 自动换行
    # style.alignment = al
    style2.alignment.wrap = 1  # 自动换行
    style2.font = font  # 设定样式

    style3 = xlwt.XFStyle()  # 初始化样式
    font = xlwt.Font()  # 为样式创建字体
    font.name = 'Times New Roman'
    font.height = 250
    font.colour_index = 2
    # style3.alignment.vert = 0x01
    # style3.alignment.horz = 0x02
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
            worksheet.col(ind).width = 10000  #列宽

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
                    annotation = annotation.strip("        ")
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

def list_file_case_id(dir):
    # 从文件中提取用例号
    sub_list = os.listdir(dir)
    for sub in sub_list:
        s = os.path.join(dir, sub)
        if os.path.isdir(s):
            list_file_case_id(s)
        elif sub.endswith(".py") and re.search("^test_", sub, re.I):
            files.append(s)

def compare_case_id():
    for file in files:
        item = re.search("_\d\d\d\d", file)
        if item :
            item = item.group()
            item = item.strip("_")
            if item and int(item) not in old:
                print(item)

if __name__ == "__main__":
    list_file_case_id(search_dir)
    compare_case_id()
    #     list_file(dir=search_dir)
    #     print(files)
    #     generate_excel(files)

