import time
class login(object):
    def __init__(self,driver):
        self.driver=driver

    def login(self):
        self.driver.find_element_by_xpath("//div[@class='el-form-item__content']/button").is_displayed()
        time.sleep(3)
        self.driver.find_element_by_class_name('el-input__inner').send_keys('15935412005')
        self.driver.find_element_by_name('password').send_keys('123456')
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[@class='el-form-item__content']/button").click()
        time.sleep(5)

    def qiyehoutai(self):


        self.driver.find_element_by_xpath("//div[@class='navbar']/span/div[2]").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//div[@class='handel-box']/button/span").click()
        time.sleep(5)