#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os,sys,re


def disposeStriping(s):
    list_demo=s.split(",")
    list_return = []
    for i in list_demo:
        item = i.replace('\n','')
        if '-' in item :
            interval=item.split("-")
            demo = list(range(int(interval[0]),int(interval[-1])+1))
            list_return.extend(demo)
        else:
            list_return.append(int(item))
    return list_return
check_hostname_cmd = 'cat /etc/hostname'
result = os.popen(check_hostname_cmd).readlines()
hostname = result[0].replace("\n","")
cmd_cpu_pin = 'cat /etc/nova/nova.conf | grep -i \'pcpu_pin\''
result = os.popen(cmd_cpu_pin).readlines()
s = result[0].replace(" ","").split("=")[-1]
pcpu_list=disposeStriping(s)

cmd_cpu_numa= 'lscpu | grep -i numa'
res2 = os.popen(cmd_cpu_numa).readlines()
s0 = res2[1].replace(" ","").split(":")[-1]
cpu_numa_0=disposeStriping(s0)
s1 = res2[2].replace(" ","").split(":")[-1]
cpu_numa_1=disposeStriping(s1)
pcpu_numa0 = []
pcpu_numa1 = []
for cpu in pcpu_list:
    if cpu in cpu_numa_0:
        pcpu_numa0.append(cpu)
    elif cpu in cpu_numa_1:
        pcpu_numa1.append(cpu)
    else:
        print("cant find %s 's numa"%cpu)

pcpu_usage_cmd = "nova hypervisor-show %s | grep -i -A 3 numa_cpu_usage"%(hostname)
os.chdir('/root')
r = os.putenv('OS_USERNAME','admin')
r = os.putenv('OS_PASSWORD','OF0WzDdpAL2g')
r = os.putenv('OS_PROJECT_NAME','admin')
r = os.putenv('OS_USER_DOMAIN_NAME','default')
r = os.putenv('OS_PROJECT_DOMAIN_NAME','default')
r = os.putenv('OS_AUTH_URL','http://10.0.40.187:35357/v3')
r = os.putenv('OS_IDENTITY_API_VERSION','3')
res3 = os.popen(pcpu_usage_cmd).readlines()

for line in res3:
    if re.search("[a-z]+",line) and  not re.search("numa_cpu_usage",line):
        num = res3.index(line)
        break
res3=res3[:num]
s3= ""      
for line in res3:
    l = line.replace(" ","").replace("|","").replace("]","").split("[")[-1]
    s3 += l
#s3 = res3[0].replace(" ","").replace("|","").replace("]","").split("[")[-1]
s3 = s3.replace("\n",",").replace(",,",",")
if s3[-1] == "," : s3 = s3[:-1]
cpu_usage = disposeStriping(s3)

def change(x):
    return int(x)
cpu_usage_int = map(change,cpu_usage)
#print(cpu_usage_int)

for cpu in cpu_usage_int:
    if cpu in pcpu_numa0:
        pcpu_numa0.remove(cpu)
    elif cpu in pcpu_numa1:
        pcpu_numa1.remove(cpu)
    else:
        print("cant find %s 's pin numa" % cpu)
print(pcpu_numa0)
print(pcpu_numa1)
print("cpu绑定：numa 0 还剩 : %s"%(str(len(pcpu_numa0))))
print("cpu绑定：numa 1 还剩 : %s"%(str(len(pcpu_numa1))))
