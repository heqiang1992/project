from auto_test_module.data_drive.excel import excel
from auto_test_module.cases.login import case_log
from auto_test_module.cases.create_notice import case_create_notice
class drive:
    def get_dict(self,row):
        dict = {}
        list = row.split("\n")
        for i in list:
            site = i.index("=")
            dict[i[:site]] =[i[site+1:]]
        return dict
    def drive_data(self):
        ex = excel()
        table = ex.read_excel("C:\\Users\\Administrator\\Desktop\\Book1.xlsx",index=1)
        for rownum in range(0,table.nrows):
            row = table.row_values(rownum)
            if row[1] =="登录"and row[2]=="登录":
                #登录模块用例
                data_dict = self.get_dict(row[4])
                case_log(data_dict["username"],data_dict["password"])
            if row[1] =="公告"and row[2]=="创建公告":
                #创建公告模块用例
                data_dict = self.get_dict(row[4])
                case_create_notice(row[0],row[5],data_dict["title"],data_dict["content"])
            if  row[1] =="公告"and row[2]=="公告管理":
                data_dict = self.get_dict(row[4])
                pass
a= drive()
a.drive_data()