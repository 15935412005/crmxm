import time
class login(object):
    def __init__(self,driver):
        self.driver=driver

    def login(self):
        time.sleep(10)
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="我的"]').click()
        time.sleep(5)
        try:
            paly = self.driver.find_element_by_xpath('//android.widget.TextView[@text="立即登录/注册"]').is_displayed()

            if  paly==True:
              self.driver.find_element_by_xpath('//android.widget.TextView[@text="立即登录/注册"]').click()
              time.sleep(3)
              self.driver.find_element_by_xpath('//android.widget.TextView[@text="密码登录"]').click()
              self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/phone_num_edit").send_keys('15127409611')
              self.driver.find_element_by_id('cn.xiaochuankeji.tieba:id/code_edit').send_keys('a123456')
              time.sleep(3)
              self.driver.find_element_by_id('cn.xiaochuankeji.tieba:id/login').click()
            else:
              pass
        except:
            pass
