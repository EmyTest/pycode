from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from loginpage1 import LoginPage
from page1 import Page



def test_user_login(driver,username,password):
    '''测试获取用户名/密码是否可以登录'''
    login_page = LoginPage(driver)
    login_page.open()
    driver.switch_to.frame("x-URS-iframe")
    login_page.type_username(username)
    login_page.type_password(password)
    login_page.submit()