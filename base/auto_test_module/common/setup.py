from selenium import webdriver
class setup:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get("http://localhost/smeoa/login/index")
