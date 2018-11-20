import time
import pymysql

def log_in(msg,type = "base"):
    server_log = open("server.log","a+")
    now_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    server_log.write(now_time+"    [%s]    "%type+str(msg)+" \n")
    server_log.close()

def create_table():
    database = pymysql.connect(host="127.0.0.1",port=3306,user="root",db="chat_room",passwd='')
    cursor = database.cursor()
    # print("hello")
    drop = "drop table if exists records"
    create = "create table records(name varchar(100),msg varchar(100),time timestamp)"
    cursor.execute(drop)
    cursor.execute(create)

def db_chat(name,msg):
    database = pymysql.connect(host="127.0.0.1",port=3306,user="root",db="chat_room",passwd='')
    cursor = database.cursor()
    sql = "insert into records(name,msg,time)" \
          "values(\""+name+"\",\""+msg+"\",now())"
    print(sql)
    cursor.execute(sql)
    # results = cursor.fetchall()     #查询所有的数据库
    # print(results)
    database.commit()
def show_record():
    database = pymysql.connect(host="127.0.0.1",port=3306,user="root",db="chat_room",passwd='')
    cursor = database.cursor()
    sql = "select * from records"
    data = cursor.execute(sql)
    database.commit()
    print(data)
# db_chat('show tables;')
