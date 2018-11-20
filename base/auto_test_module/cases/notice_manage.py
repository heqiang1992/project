from auto_test_module.common.notice import notice
#用例公告管理-001
try:
    case_001 = notice()
    case_001.notice_manage("this is title")
    case_001.manage_assert()
    case_001.quit()
except:
    print("case_001 failed")