
#链接MySQL数据库
import pymysql
# 打开数据库连接
database = pymysql.connect("localhost","test_user")
# 关闭数据库
database.close()
# 使用 cursor() 方法创建一个游标对象 cursor
#  ●声明游标
#  ●打开游标
#  ●从游标中操作数据
#  ●关闭游标
cursor = database.cursor()
# 使用预处理语句创建表
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,
         SEX CHAR(1),
         INCOME FLOAT )"""
cursor.execute(sql)
# 使用 execute() 方法执行 SQL，如果表存在则删除
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
# SQL 插入语句
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   database.commit()
except:
   # 如果发生错误则回滚
   database.rollback()
