from appium import webdriver
import time
import os
import unittest
from public.applogin import Mylogin

PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))

class AndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps={}
        desired_caps['platformName']='Android'
        desired_caps['platformVersion']='5.1'
        desired_caps['deviceName']='Android Emulator'
        desired_caps['noReset']='True'
        desired_caps['app']=PATH('D:/newCourse/zuiyou518.apk')
        desired_caps['appPackage']='cn.xiaochuankeji.tieba'
        desired_caps['appActivity']='.ui.home.page.PageMainActivity'
        self.driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

    def tearDown(self):
        self.driver.quit()


    def test1(self):
        Mylogin(self.driver).login()
        dd=self.driver.find_element_by_xpath('//android.widget.ImageView[@resource-id=cn.xiaochuankeji.tieba:id/middle_view]')
        dd.text()

if __name__=="__main__":
    unittest.main()