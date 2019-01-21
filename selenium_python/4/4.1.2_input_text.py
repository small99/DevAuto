# -*- coding: utf-8 -*-

__author__ = "苦叶子"


from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


if __name__ == "__main__":

    driver = webdriver.Chrome()
    action_chains = ActionChains(driver)
    driver.get("http://www.python.org")

    # 查找输入框
    ele = driver.find_element_by_name("q")
    action_chains.send_keys_to_element(ele, "list")

    # 查找GO按钮
    btn = driver.find_element_by_id("submit")
    action_chains.send_keys_to_element(btn, Keys.RETURN)
    action_chains.pause(2)

    # 执行动作链
    action_chains.perform()

    # 清空动作链
    action_chains.reset_actions()

    # 换个搜索词
    ele = driver.find_element_by_id("id-search-field")
    ele.clear()
    action_chains.send_keys_to_element(ele, "tuple")

    # 输入回车
    btn = driver.find_element_by_id("submit")
    action_chains.send_keys_to_element(btn, Keys.RETURN)
    action_chains.pause(2)

    # 执行动作链
    action_chains.perform()

    driver.quit()
