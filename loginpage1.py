from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from page1 import Page
import time


class LoginPage(Page):
    '''
    126邮箱登录页面模型
    '''
    url = '/'
    # driver = webdriver.Chrome()
    # driver.switch_to.frame("x-URS-iframe")
    # driver.find_element_by_name("email").clear()
    # driver.find_element_by_name("email").send_keys("mg5851")
    # driver.find_element_by_name("password").clear()
    # driver.find_element_by_name("password").send_keys("yuyu0110")
    # driver.find_element_by_id("dologin").click()

    username_loc = (By.NAME,"email")
    password_loc = (By.NAME,"password")
    submit_loc = (By.ID,"dologin")

    #Action
    def type_username(self,username):

        self.find_element(*self.username_loc).send_keys(username)
    def type_password(self,password):

        self.find_element(*self.password_loc).send_keys(password)
    def submit(self):

        self.find_element(*self.submit_loc).click()