# -*- coding: utf-8 -*-

__author__ = "苦叶子"


from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


if __name__ == "__main__":

    driver = webdriver.Chrome()
    driver.get("http://www.python.org")

    # 查找输入框
    ele = driver.find_element_by_name("q")
    print(ele)

    # 输入str()
    ele.send_keys("str()")
    sleep(1)

    # 查找GO按钮
    btn = driver.find_element_by_id("submit")
    print(btn)

    # 输入回车
    btn.send_keys(Keys.RETURN)
    sleep(2)

    # 清空输入框，换个搜索词
    ele = driver.find_element_by_id("id-search-field")
    ele.clear()
    ele.send_keys("list")

    # 输入回车
    btn = driver.find_element_by_id("submit")
    btn.send_keys(Keys.RETURN)
    sleep(2)

    driver.quit()
