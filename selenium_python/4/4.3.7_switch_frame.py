# -*- coding: utf-8 -*-

__author__ = "苦叶子"


from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains


# 切换至默认的frame上下文环境
def switch_default_frame(driver):
    driver.switch_to.default_content()

    # 定位下alert_id按钮
    ele = driver.find_element_by_id("alert_id")
    print(ele)


# 获取父frame
def switch_parent_frame(driver):
    driver.switch_to.parent_frame()
    # 定位下alert_id按钮
    ele = driver.find_element_by_id("alert_id")
    print(ele)


# 切换至指定的frame
def switch_frame(driver):
    # 通过name属性切换
    driver.switch_to.frame('baidu')
    # 通过索引切换
    # driver.switch_to.frame(1)
    # 通过定位的元素切换
    # driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0])
    # 定位下百度一下按钮
    ele = driver.find_element_by_id("su")
    print(ele)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    action_chains = ActionChains(driver)

    driver.get("file:///Users/lyy/Documents/project/DevAuto/selenium_python/4/demo.html")

    # 1
    switch_frame(driver)
    switch_default_frame(driver)

    sleep(2)

    # 2
    switch_frame(driver)
    switch_parent_frame(driver)

    sleep(3)

    driver.quit()
