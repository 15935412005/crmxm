#coding=utf-8
from selenium import webdriver
import time
import os
import unittest
class Testdenglu(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get('http://101.133.169.100:8088/index.html#/login?redirect=%2F404')
        self.driver.maximize_window()
        time.sleep(6)
        print('starttime:'+time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))

    def tearDown(self):
        filedir='D:\pycharm_bcbx\crmxm1'
        if os.path.exists(filedir):
            os.makedirs(os.path.join('D:/','pycharm_bcbx','crmxm1'))
        print('endtime:'+time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))
        screen_name = filedir + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + ".png"
        self.driver.get_screenshot_as_file(screen_name)
        self.driver.quit()

    def testwkcrm001(self):
        '''登录-检查登录页面 '''
        denglu=self.driver.find_element_by_xpath("//div[@class='el-form-item__content']/button").is_displayed()
        zhanghu=self.driver.find_element_by_class_name('el-input__inner').is_displayed()
        password=self.driver.find_element_by_name('password').is_displayed()

        self.assertTrue('denglu')
        self.assertTrue('zhanghu')
        self.assertTrue('password')


    def wkcrm002(self):
        '''登录-输入系统中已存在的用户'''
        zhanghu=self.driver.find_element_by_class_name('el-input__inner').send_keys('15935412005')
        password=self.driver.find_element_by_name('password').send_keys('123456')
        dl=self.driver.find_element_by_xpath("//div[@class='el-form-item__content']/button").click()
        time.sleep(4)

        zh=self.driver.find_element_by_class_name('el-input__inner').get_attribute('value')
        pw=self.driver.find_element_by_name('password').get_attribute('value')
        self.assertEqual('15935412005',zh)
        self.assertEqual('123456',pw)



if __name__=="__main__":
    unittest.main()
