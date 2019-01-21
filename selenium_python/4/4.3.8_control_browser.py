# -*- coding: utf-8 -*-

__author__ = "苦叶子"


from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains



if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    action_chains = ActionChains(driver)

    # 访问百度首页
    driver.get("http://www.baidu.com")
    sleep(1)

    # 点击下新闻链接
    ele = driver.find_element_by_link_text("新闻")
    action_chains.click(ele).perform()
    sleep(3)

    # 最小化浏览器窗口
    driver.minimize_window()
    sleep(1)

    # 最大化浏览器窗口
    driver.maximize_window()
    sleep(1)

    # 设置浏览器窗口大小为 800 x 600
    driver.set_window_size(800, 600)
    sleep(1)

    # back动作
    driver.back()
    sleep(1)

    # forward动作
    driver.forward()
    sleep(1)

    # refresh动作
    driver.refresh()

    sleep(3)

    driver.quit()
