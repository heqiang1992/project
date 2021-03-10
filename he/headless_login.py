# -*- coding:utf-8 -*-
__autthor__ = "heqiang"

from selenium import webdriver
import os, time, sys
import threading
import random

error_num = 0
gLock = threading.Lock()
users = ["user001", "user002", "user4","user005","user006","user008"]


def demo():
    try:
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        # driver = webdriver.Chrome()
        driver = webdriver.Chrome(options=option)
        url = "http://10.0.9.43:3000/"
        driver.get(url=url)
        # driver.maximize_window()
        driver.implicitly_wait(10)
        # search_input = driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/div[3]/div/div[2]/div[1]/div")
        driver.find_element_by_id("rc_select_0").click()
        time.sleep(3)
        js = "document.getElementById(\"rc_select_0\").setAttribute(\"aria-activedescendant\",\"rc_select_0_list_2\")"
        driver.execute_script(js)
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/div/div/div[3]/div/div/div[1]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/div[3]/div/div[2]/div[2]/i").click()
        time.sleep(2)
        driver.find_element_by_id("username").clear()
        global users
        name = random.choice(users)
        driver.find_element_by_id("username").send_keys(name)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("123456")
        driver.find_element_by_id("dt_kc-login").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/div[2]/div/div[2]/div")
    except:
        gLock.acquire()
        global error_num
        error_num += 1
        gLock.release()
        driver.close()
    else:
        driver.close()


num = sys.argv[1]
threads = []
for i in range(int(num)):
    t = threading.Thread(target=demo)
    t.setDaemon(True)
    threads.append(t)
    t.start()
for sub in threads:
    sub.join()

print(error_num)
