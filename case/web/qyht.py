#coding=utf-8
from selenium import webdriver
import time
from public.login import login
import os
import unittest
from selenium.webdriver.support.select import Select

class Testqiyehoutai(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://101.133.169.100:8088/index.html#/login?redirect=%2F404')
        self.driver.maximize_window()
        time.sleep(5)
        print('starttime:' + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))

    def tearDown(self):
        filedir = 'D:\pycharm_bcbx\crmxm1'
        if os.path.exists(filedir):
            os.makedirs(os.path.join('D:/', 'pycharm_bcbx', 'crmxm1'))
        print('endtime:' + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))
        screen_name = filedir + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + ".png"
        self.driver.get_screenshot_as_file(screen_name)
        self.driver.quit()

    def testwkcrm011(self):
        '''检查点击“个人头像”'''
        login(self.driver).login()
        self.driver.find_element_by_xpath("//div[@class='photo-wrap']/div").click()
        time.sleep(3)
        grzx=self.driver.find_element_by_xpath("//div[text()='个人中心']").is_displayed()
        tcdl= self.driver.find_element_by_xpath("//div[text()='退出登录']").is_displayed()
        qyglht = self.driver.find_element_by_xpath("//div[@class='handel-box']/button/span").is_displayed()

        self.assertTrue(grzx)
        self.assertTrue(tcdl)
        self.assertTrue(qyglht)

    def  testwkcrm014(self):
        '''检查“返回首页”按钮'''
        login(self.driver).login()
        login(self.driver).qiyehoutai()
        time.sleep(5)
        self.driver.find_element_by_xpath("//div[@class='back-home']").click()
        time.sleep(5)
        url=print(self.driver.current_url)
        bg=self.driver.find_element_by_link_text('办公')


        self.assertEqual('办公',bg.text)
        self.assertTrue('http://101.133.169.100:8088/index.html#/workbench/index',url)


    def testwkcrm015(self):
        '''确定“退出系统”'''
        login(self.driver).login()
        login(self.driver).qiyehoutai()
        self.driver.find_element_by_xpath("//div[@class='go-out']").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//div[@class='el-message-box__btns']/button[2]/span").click()
        time.sleep(5)
        url = print(self.driver.current_url)

        self.assertTrue('http://101.133.169.100:8088/index.html#/login', url)

    def testwkcrm016(self):
        '''取消“退出系统”'''
        login(self.driver).login()
        login(self.driver).qiyehoutai()
        self.driver.find_element_by_xpath("//div[@class='go-out']").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//div[@class='el-message-box__btns']/button[1]/span").click()
        time.sleep(5)
        url = print(self.driver.current_url)

        self.assertTrue('http://101.133.169.100:8088/index.html#/manager/systemconfig', url)



    def testwkcrm017(self):
         '''检查“员工与部门管理”页面'''
         login(self.driver).login()
         login(self.driver).qiyehoutai()
         self.driver.find_element_by_xpath("//div[@class='container']/ul/a/li").click()
         time.sleep(3)
         url = print(self.driver.current_url)
         self.assertTrue('http://101.133.169.100:8088/index.html#/manager/employee-dep')




    def testwkcrm038(self):
         '''“新建员工”密码填写6-12字符含“汉字”'''
         login(self.driver).login()
         login(self.driver).qiyehoutai()
         self.driver.find_element_by_xpath('//*[@id="app"]/section/section/aside/div/ul/a[3]/li').click()
         time.sleep(5)
         self.driver.find_element_by_xpath("//div[@class='table-top']/button").click()
         self.driver.implicitly_wait(50)
         self.driver.find_element_by_xpath("//div[@class='el-dialog']/div/form/div[1]/div/div/input").send_keys('15935412006')

         self.driver.find_element_by_xpath("//div[@class='el-dialog']/div/form/div[2]/div/div/input").send_keys('12w@.98好')

         self.driver.find_element_by_xpath("//div[@class='el-dialog']/div/form/div[3]/div/div/input").send_keys('迪丽热嘛')
         # s=self.driver.find_element_by_xpath("//div[@class='el-dialog__body']/form/div[6]/div/div/div/input").click()
         # Select(s).select_by_index(3)
         self.driver.find_element_by_xpath("//div[@class='el-dialog__body']/form/div[9]/div/div/div[2]/input").click()
         self.driver.find_element_by_xpath("//div[@class='el-dialog']/div/form/div[9]/div/div/div[3]/div[1]/div[1]/ul/ul[1]/li[2]/ul/li[1]").click()
         self.driver.find_element_by_link_text('保存').click()

         aa=self.driver.find_element_by_xpath('/html/body/div[3]').is_displayed()

         self.assertFalse(aa)













if __name__=="__main__":
    unittest.main()

