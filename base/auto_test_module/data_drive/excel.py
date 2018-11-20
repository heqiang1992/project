import xlrd,sys,xdrlib
class excel:
    def read_excel(self,file_path,index=0):
        data = xlrd.open_workbook(file_path)
        sheet = data.sheets()[index]
        return sheet


class test_case():
    def __init__(self):
        pass


class TEST(test_case):

    def pro_set(self):
        super(TEST,self).pro_set()
        pass