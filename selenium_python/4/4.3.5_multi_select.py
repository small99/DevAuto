# -*- coding: utf-8 -*-

__author__ = "苦叶子"


from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select


# 演示基本功能, 然后取消选中
def select_basic(ele):
    # 通过索引选中第一个
    Select(ele).select_by_index(0)
    sleep(1)

    # 通过value选中第2个
    Select(ele).select_by_value("value_2")
    sleep(1)

    # 通过文本选中第3个
    Select(ele).select_by_visible_text("测试数据3")
    sleep(1)

    # 取消已选中的项
    Select(ele).deselect_all()
    sleep(1)


# 通过文本选中所有项, 然后取消选中
def select_all_by_text(ele):
    # 获取所有选项, 下面两种方式均可实现
    options = Select(ele).options
    # options = Select(ele).all_selected_options

    # 通过文本选中所有项
    for o in options:
        Select(ele).select_by_visible_text(o.text)
        sleep(0.5)

    # 取消已选中的项
    Select(ele).deselect_all()
    sleep(1)


# 通过索引选中所有项, 然后取消选中
def select_all_by_index(ele):
    # 获取所有选项, 下面两种方式均可实现
    options = Select(ele).options
    for i in range(0, len(options)):
        Select(ele).select_by_index(i)
        sleep(0.5)
    # 取消已选中的项
    Select(ele).deselect_all()
    sleep(1)


# 通过value选中所有项, 然后取消选中
def select_all_by_value(ele):
    # 获取所有选项, 下面两种方式均可实现
    options = Select(ele).options
    # options = Select(ele).all_selected_options

    # 通过文本选中所有项
    for o in options:
        Select(ele).select_by_value(o.get_attribute("value"))
        sleep(0.5)

    # 取消已选中的项
    Select(ele).deselect_all()
    sleep(1)


if __name__ == "__main__":

    driver = webdriver.Chrome()
    action_chains = ActionChains(driver)
    driver.get("file:///Users/lyy/Documents/project/DevAuto/selenium_python/4/demo.html")

    ele = driver.find_element_by_id("multi_select_id")

    select_basic(ele)

    select_all_by_text(ele)

    select_all_by_index(ele)

    select_all_by_value(ele)

    sleep(3)

    driver.quit()
