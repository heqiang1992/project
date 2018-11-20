from auto_test_module.common.notice import notice
def case_create_notice(case_num,expected,title="",content=""):
    try:
        create_notice_001 = notice()
        create_notice_001.create(title,content)
        create_notice_001.create_judge(case_num,expected)
    except:
        print("case didn't passed ",case_num)
    else:
        print("case passed ",case_num)
#用例001
# case_create_notice("create_notice_001","title","content")
# #用例002
# try:
#     create_notice_002 = notice()
#     create_notice_002.create("","every body hi hi hi hi hi")
#     create_notice_002.create_judge("create_notice-002")
# except:
#     print("case:create_notice-001 failed")