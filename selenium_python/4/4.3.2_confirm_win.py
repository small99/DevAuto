# -*- coding: utf-8 -*-

__author__ = "苦叶子"


from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains


# 按下确定按钮关闭弹窗
def click_accept(driver, action_chains):
    # 注意这里./demo.html一定要改为你实际的demo.html位置
    driver.get("file:///Users/lyy/Documents/project/DevAuto/selenium_python/4/demo.html")

    # 单击confirm按钮，弹出confirm窗口
    confirm_btn = driver.find_element_by_id("confirm_id")
    action_chains.click(confirm_btn).perform()

    # 捕获confirm窗口
    confirm_win = driver.switch_to.alert

    # 打印下confirm窗口文本
    print("confirm text is [%s] " % confirm_win.text)

    sleep(1)

    # 按下confirm窗口的确定按钮，关闭confirm窗口
    confirm_win.accept()


# 按下取消按钮关闭弹窗
def click_cancel(driver, action_chains):
    # 注意这里./demo.html一定要改为你实际的demo.html位置
    driver.get("file:///Users/lyy/Documents/project/DevAuto/selenium_python/4/demo.html")

    # 单击confirm按钮，弹出confirm窗口
    confirm_btn = driver.find_element_by_id("confirm_id")

    # 重置action_chains
    action_chains.reset_actions()
    action_chains.click(confirm_btn).perform()

    # 捕获confirm窗口
    confirm_win = driver.switch_to.alert

    # 打印下confirm窗口文本
    print("confirm text is [%s] " % confirm_win.text)

    sleep(1)

    # 按下confirm窗口的取消按钮，关闭confirmc窗口
    confirm_win.dismiss()

    sleep(2)


if __name__ == "__main__":

    driver = webdriver.Chrome()
    action_chains = ActionChains(driver)

    click_accept(driver, action_chains)

    sleep(2)

    click_cancel(driver, action_chains)

    driver.quit()
