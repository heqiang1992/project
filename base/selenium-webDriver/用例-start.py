import os
file_list = os.listdir("D:\\heqiang\\pythonstudy\\selenium-webDriver\\现行脚本自动化-论坛发帖")
for file in file_list:
    if file.split(".")[1] == "py":
        os.system('python D:\\heqiang\\pythonstudy\\selenium-webDriver\\现行脚本自动化-论坛发帖\\%s'%file)