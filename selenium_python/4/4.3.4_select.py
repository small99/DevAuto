# -*- coding: utf-8 -*-

__author__ = "苦叶子"


from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select


if __name__ == "__main__":

    driver = webdriver.Chrome()
    action_chains = ActionChains(driver)
    driver.get("file:///Users/lyy/Documents/project/DevAuto/selenium_python/4/demo.html")

    ele = driver.find_element_by_id("select_id")

    # 通过索引选中第一个
    Select(ele).select_by_index(0)
    sleep(2)

    # 通过value选中第2个
    Select(ele).select_by_value("value_2")
    sleep(2)

    # 通过文本选中第3个
    Select(ele).select_by_visible_text("测试数据3")
    sleep(2)

    driver.quit()
