from auto_test_module.common.setup import setup
from auto_test_module.common.login import login
from selenium import webdriver
def case_log(admin="",password=""):
    print(admin[2:-2])
    print(password[2:-2])
    try:
        log=login()
        log.login_start(admin,password)
        log.ASSERT()
        log.quit()
    except:
        print("case didn't passed")
    else:
        print("case passed")
#用例登录-001：
# case_log("admin","admin")
#用例登录-002：
# try:
# login().login_start("","admin")
# login().judge()
# login().quit()
# #用例登录-003：
# try:
#     login3 =login()
#     login3.login_start("admin","")
#     login3.quit()
# except:
#     pass
# #用例登录-004：
# login4=login()
# login4.login_start("55555","admin")
# login4.quit()
