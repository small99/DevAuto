# -*- coding: utf-8 -*-

__author__ = "苦叶子"


from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains


def switch_to_win_1(driver):
    # 遍历所有windows handles，查找目标, 方式一
    handles = driver.window_handles
    index = 0
    for index in range(0, len(handles)):
        driver.switch_to.window(handles[index])
        if "百度一下，你就知道" in driver.title:
            break

    print(driver.title)


def switch_to_win_2(driver):
    handles = driver.window_handles
    for handle in handles:
        driver.switch(handle)
        if "百度一下，你就知道" in driver.title:
            break

    print(driver.title)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    action_chains = ActionChains(driver)

    driver.get("file:///Users/lyy/Documents/project/DevAuto/selenium_python/4/demo.html")

    # 打开b百度
    ele = driver.find_element_by_link_text("打开百度")
    action_chains.click(ele)

    action_chains.perform()

    # 获取当前window handle
    cur_handle = driver.current_window_handle

    # 方式一
    switch_to_win_1(driver)

    sleep(3)

    # 方式二
    switch_to_win_2(driver)

    sleep(3)

    driver.quit()
