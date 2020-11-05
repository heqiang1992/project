# -*- coding:utf-8 -*-
__autthor__ = "heqiang"

from selenium import webdriver
import os, time
from selenium.webdriver.common.action_chains import ActionChains

option = webdriver.ChromeOptions()
option.add_argument('headless')

# screen_path = os.path.dirname(os.getcwd()) +'/report/Screenshots/'
# rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
# screen_name = screen_path + rq + '.png'


driver = webdriver.Chrome()

# driver = webdriver.Chrome(options = option)

url = "http://10.0.9.43:3000/"
# url = 'http://10.0.9.43:9535/auth/realms/zhuhu/protocol/openid-connect/auth?client_id=unicorn-admin-console&redirect_uri=http%3A%2F%2F10.0.9.43%3A3000%2F%23%2Flaunchpad%3F&state=9daead1e-d757-406e-91b3-eebc4399207b&response_mode=fragment&response_type=code&scope=openid&nonce=b59574ae-95d2-4712-8f50-ccbcc90082b2&code_challenge=nnjOSWPVzN-5xJDSp0AT0YLHv8egB4EpqSEYjRYhIQY&code_challenge_method=S256'

driver.get(url=url)
driver.maximize_window()
driver.implicitly_wait(10)
search_input = driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/div[3]/div/div[2]/div[1]/div")
# str = driver.execute_script("return arguments[7].value = 'rc_select_0_list_0';", search_input)


# str = driver.execute_script("return arguments[11].value = 'false';", search_input)
# search_input.setAttribute("aria-expanded", "true")
# js = "document.getElementById(\"rc_select_0\").setAttribute(\"aria-expanded\",\"true\")"
# driver.execute_script(js)
# driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/div[3]/div/div[2]/div[1]/div").click()
driver.find_element_by_id("rc_select_0").click()
time.sleep(3)
js = "document.getElementById(\"rc_select_0\").setAttribute(\"aria-activedescendant\",\"rc_select_0_list_2\")"
driver.execute_script(js)
status = driver.find_element_by_id("rc_select_0").get_attribute("aria-activedescendant")
print(status)
# move = driver.find_element_by_id("rc_select_0")
# ActionChains(driver).click(move).perform()
# driver.find_element_by_id("rc_select_0").click()
driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/div/div/div[3]/div/div/div[1]").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/div[3]/div/div[2]/div[2]/i").click()
time.sleep(3)
driver.find_element_by_id("username").clear()
driver.find_element_by_id("username").send_keys("user001")
driver.find_element_by_id("password").clear()
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_id("dt_kc-login").click()
# time.sleep(3)
# # driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/div[2]/div/div[2]")
#
#
# # driver.save_screenshot(screen_name)
time.sleep(10)


# 退出并关闭浏览器
driver.quit()
