from threading import Thread
from selenium import webdriver
from time import ctime,sleep

def test_baidu(browser,search):
    print('Start:%s' %ctime())
    print('browser:%s,'%browser)
    if browser == "ie":
        driver = webdriver.Ie()
    elif browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "ff":
        driver = webdriver.Firefox()
    else:
        print("browser 参数有误，只能为ie、ff、chrome")
    driver.get('http://www.baidu.com')
    driver.find_element_by_id("kw").send_keys(search)
    driver.find_element_by_id("su").click()
    sleep(2)
    driver.quit()
if __name__=='__main__':
    lists = {'chrome':'threading','ie':'webdriver','ff':'python'}

    threads = []
    files = range(len(lists))

    for browser,search in lists.items():
        t = Thread(target=test_baidu,args=(browser,search))
        threads.append(t)
    for t in files:
        threads[t].start()
    for t in files:
        threads[t].join()
    print('end:%s'%ctime())