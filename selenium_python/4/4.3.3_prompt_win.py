# -*- coding: utf-8 -*-

__author__ = "苦叶子"


from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains


# 按下确定按钮关闭弹窗
def click_accept(driver, action_chains):
    # 注意这里./demo.html一定要改为你实际的demo.html位置
    driver.get("file:///Users/lyy/Documents/project/DevAuto/selenium_python/4/demo.html")

    # 单击prompt按钮，弹出prompt窗口
    prompt_btn = driver.find_element_by_id("prompt_id")
    action_chains.click(prompt_btn).perform()

    # 捕获prompt窗口
    prompt_win = driver.switch_to.alert

    # 打印下prompt窗口文本
    print("prompt text is [%s] " % prompt_win.text)

    sleep(1)

    # 按下prompt窗口的确定按钮，关闭prompt窗口
    prompt_win.accept()


# 按下取消按钮关闭弹窗
def click_cancel(driver, action_chains):
    # 注意这里./demo.html一定要改为你实际的demo.html位置
    driver.get("file:///Users/lyy/Documents/project/DevAuto/selenium_python/4/demo.html")

    # 单击prompt按钮，弹出prompt窗口
    prompt_btn = driver.find_element_by_id("prompt_id")

    # 重置action_chains
    action_chains.reset_actions()
    action_chains.click(prompt_btn).perform()

    # 捕获prompt窗口
    prompt_win = driver.switch_to.alert

    # 打印下prompt窗口文本
    print("prompt text is [%s] " % prompt_win.text)

    sleep(1)

    # 按下prompt窗口的取消按钮，关闭promptc窗口
    prompt_win.dismiss()

    sleep(2)


# 给prompt窗体输入自定义文本
def send_keys(driver, action_chains, text):
    # 注意这里./demo.html一定要改为你实际的demo.html位置
    driver.get("file:///Users/lyy/Documents/project/DevAuto/selenium_python/4/demo.html")

    # 单击prompt按钮，弹出prompt窗口
    prompt_btn = driver.find_element_by_id("prompt_id")

    # 重置action_chains
    action_chains.reset_actions()
    action_chains.click(prompt_btn).perform()

    # 捕获prompt窗口
    prompt_win = driver.switch_to.alert

    # 打印下prompt窗口文本
    print("prompt text is [%s] " % prompt_win.text)
    prompt_win.send_keys(text)

    sleep(1)

    # 按下prompt窗口的取消按钮，关闭promptc窗口
    prompt_win.accept()

    sleep(2)


if __name__ == "__main__":

    driver = webdriver.Chrome()
    action_chains = ActionChains(driver)

    # 点击确定关闭
    click_accept(driver, action_chains)
    sleep(2)

    # 点击取消关闭
    click_cancel(driver, action_chains)
    sleep(2)

    # 输入文本
    send_keys(driver, action_chains, "我的公众号ID是： DeepTest")
    sleep(2)

    driver.quit()
