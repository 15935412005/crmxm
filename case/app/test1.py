from appium import webdriver
import time
import os
import unittest
from public.applogin import login

class AndroidTest(unittest.TestCase):
    def setUp(self):
        desired_caps={}
        desired_caps['platformName']='Android'
        desired_caps['platformVersion']='5.1'
        desired_caps['deviceName']='Android Emulator'
        desired_caps['noReset']='True'
        desired_caps['appPackage']='cn.xiaochuankeji.tieba'
        desired_caps['appActivity']='.ui.base.SplashActivity'
        self.driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)


    def tearDown(self):
        self.driver.quit()

    def test1(self):
        login(self.driver).login()
        time.sleep(10)
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="最右"]').click()
        time.sleep(5)
        size=self.driver.get_window_size()
        height=size['height']
        width=size['width']
        self.driver.swipe(width*0.5,height*0.1,width*0.5,height*0.9,5000)
        time.sleep(5)




if __name__=='__main__':
    unittest.main()

















