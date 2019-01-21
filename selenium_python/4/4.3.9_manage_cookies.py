# -*- coding: utf-8 -*-

__author__ = "苦叶子"


from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    action_chains = ActionChains(driver)

    driver.get("http://www.baidu.com")
    sleep(3)

    # 默认的cookies为空
    cookies = driver.get_cookies()
    print(cookies)

    # 新增一些cookies
    driver.add_cookie({'name': 'foo', 'value': 'bar', 'path': '/', 'secure': True})

    # 再次获取所有cookies
    cookies = driver.get_cookies()
    print(cookies)

    # 删除指定的cookie
    driver.delete_cookie("name")
    # 再次获取所有cookies
    cookies = driver.get_cookies()
    print(cookies)

    # 获取指定的cookie
    # 注意要根据实际返回的cookie的数据结构来决定用下面的方式还是用get_cookie方法
    cookie = driver.get_cookies()[0]["value"]
    print(cookie)

    # 清空cookies
    driver.delete_all_cookies()
    cookies = driver.get_cookies()
    print(cookies)

    driver.quit()
