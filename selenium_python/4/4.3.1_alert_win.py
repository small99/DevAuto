# -*- coding: utf-8 -*-

__author__ = "苦叶子"


from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains


if __name__ == "__main__":

    driver = webdriver.Chrome()
    action_chains = ActionChains(driver)

    # 注意这里./demo.html一定要改为你实际的demo.html位置
    driver.get("file:///Users/lyy/Documents/project/DevAuto/selenium_python/4/demo.html")

    # 单击alert按钮，弹出alert窗口
    alert_btn = driver.find_element_by_id("alert_id")
    action_chains.click(alert_btn).perform()

    # 捕获alert窗口
    alert_win = driver.switch_to.alert

    # 打印下alert窗口文本
    print("alert text is [%s] " % alert_win.text)

    sleep(2)

    # 按下alert窗口的确定按钮，关闭alertc窗口
    alert_win.accept()

    sleep(2)

    driver.quit()
