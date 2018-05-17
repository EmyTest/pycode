from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from testuserlg1 import test_user_login
from page1 import Page

def main():
    try:
        driver = webdriver.Chrome()
        # driver.switch_to.frame("x-URS-iframe")
        username = 'mg5851'
        password = 'yuyu0110'
        test_user_login(driver,username,password)
        sleep(3)
        text = driver.find_element_by_xpath("//span[@id='spnUid']").text
        assert(text == 'mg5851@126.com'),"用户名称不匹配，登录失败！"
    finally:
        '''关闭浏览器窗口'''
        driver.close()
if __name__=='__main__':
    main()

