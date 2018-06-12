import time
import datetime
"""
datetime模块用于是date和time模块的合集，datetime有两个常量，MAXYEAR和MINYEAR，分别是9999和1.

datetime模块定义了5个类，分别是

datetime.date：表示日期的类

datetime.datetime：表示日期时间的类

datetime.time：表示时间的类

datetime.timedelta：表示时间间隔，即两个时间点的间隔

datetime.tzinfo：时区的相关信息

一、首先看一下datetime.date类：

date类有三个参数, datetime.date(year, month, day)，返回year - month - day
方法：
1.
datetime.date.ctime(), 返回格式如
Sun
Apr
16
00:00:00
2017

2.datetime.date.fromtimestamp(timestamp), 根据给定的时间戮，返回一个date对象；datetime.date.today()
作用相同

3.datetime.date.isocalendar():返回格式如(year，month，day)的元组, (2017, 15, 6)

4.datetime.date.isoformat()：返回格式如YYYY - MM - DD

5.datetime.date.isoweekday()：返回给定日期的星期（0 - 6），星期一 = 0，星期日 = 6

6.datetime.date.replace(year, month, day)：替换给定日期，但不改变原日期

7.datetime.date.strftime(format):把日期时间按照给定的format进行格式化。

8.datetime.date.timetuple()：返回日期对应的time.struct_time对象

　　time.struct_time(tm_year=2017, tm_mon=4, tm_mday=15, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=5, tm_yday=105,
                   tm_isdst=-1)
            
datetime.date.weekday()：返回日期的星期
python中时间日期格式化符号：
% y
两位数的年份表示（00 - 99）
% Y
四位数的年份表示（000 - 9999）
% m月份（01 - 12）
% d
月内中的一天（0 - 31）
% H
24小时制小时数（0 - 23）
% I
12
小时制小时数（01 - 12）
% M
分钟数（00 = 59）
% S
秒（00 - 59）
% a
本地简化星期名称
% A
本地完整星期名称
% b
本地简化的月份名称
% B
本地完整的月份名称
% c
本地相应的日期表示和时间表示

% j
年内的一天（001 - 366）
% p
本地A.M.或P.M.的等价符
% U
一年中的星期数（00 - 53）星期天为星期的开始
% w
星期（0 - 6），星期天为星期的开始
% W
一年中的星期数（00 - 53）星期一为星期的开始
% x
本地相应的日期表示
% X
本地相应的时间表示
% Z
当前时区的名称
% % % 号本身

二、看一下datetime的time类

time类有5个参数，datetime.time(hour, minute, second, microsecond, tzoninfo), 返回08:29:30

1.datetime.time.replace()

2.datetime.time.strftime(format):按照format格式返回时间

3.datetime.time.tzname()：返回时区名字

4.datetime.time.utcoffset()：返回时区的时间偏移量

三、datetime的datetime类

datetime类有很多参数，datetime(year, month, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]])，返回年月日，时分秒

datetime.datetime.ctime()

datetime.datetime.now().date()：返回当前日期时间的日期部分

datetime.datetime.now().time()：返回当前日期时间的时间部分

datetime.datetime.fromtimestamp()

datetime.datetime.now()：返回当前系统时间

datetime.datetime.replace()

datetime.datetime.strftime()：由日期格式转化为字符串格式

　　datetime.datetime.now().strftime('%b-%d-%Y %H:%M:%S')
　　'Apr-16-2017 21:01:35'

datetime.datetime.strptime():由字符串格式转化为日期格式

datetime.datetime.strptime('Apr-16-2017 21:01:35', '%b-%d-%Y %H:%M:%S')
2017 - 04 - 16
21:01:35
四、datetime的timedelta类
datetime.datetime.timedelta用于计算两个日期之间的差值，例如：
>> > a = datetime.datetime.now()
>> > b = datetime.datetime.now()
>> > a
datetime.datetime(2017, 4, 16, 21, 21, 20, 871000)
>> > b
datetime.datetime(2017, 4, 16, 21, 21, 29, 603000)
>> > b - a
datetime.timedelta(0, 8, 732000)
>> > (b - a).seconds
8
或者
time1 = datetime.datetime(2016, 10, 20)
time2 = datetime.datetime(2015, 11, 2)
#计算天数差值
print(time1 - time2).days
#计算两个日期之间相隔的秒数
print (time1 - time2).total_seconds()
"""
def yes_time():
    #获取当前时间
    now_time = datetime.datetime.now()
    #当前时间减去一天 获得昨天当前时间
    yes_time = now_time + datetime.timedelta(days=-1)
    #格式化输出
    yes_time_str = yes_time.strftime('%Y-%m-%d %H:%M:%S')
    print yes_time_str  # 2017-11-01 22:56:02

def dif_time():
    #计算两个时间之间差值
    now_time = datetime.datetime.now()
    now_time = now_time.strftime('%Y-%m-%d %H:%M:%S')
    d1 = datetime.datetime.strptime('2017-10-16 19:21:22', '%Y-%m-%d %H:%M:%S')
    d2 = datetime.datetime.strptime(now_time, '%Y-%m-%d %H:%M:%S')
    #间隔天数
    day = (d2 - d1).days
    #间隔秒数
    second = (d2 - d1).seconds
    print day   #17
    print second  #13475  注意这样计算出的秒数只有小时之后的计算额 也就是不包含天之间差数

def unix_time():
    #将python的datetime转换为unix时间戳
    dtime = datetime.datetime.now()
    un_time = time.mktime(dtime.timetuple())
    print un_time  #1509636609.0
    #将unix时间戳转换为python  的datetime
    unix_ts = 1509636585.0
    times = datetime.datetime.fromtimestamp(unix_ts)
    print times  #2017-11-02 23:29:45