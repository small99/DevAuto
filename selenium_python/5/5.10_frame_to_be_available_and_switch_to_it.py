# -*- coding: utf-8 -*-

__author__ = "苦叶子"

from selenium import webdriver

# 导入WebDriverWait类
from selenium.webdriver.support.ui import WebDriverWait

# 导入定位方式
from selenium.webdriver.common.by import By

# 导入
from selenium.webdriver.support.expected_conditions import frame_to_be_available_and_switch_to_it


if __name__ == "__main__":
    driver = webdriver.Chrome()

    # 构建WebDriverWait对象
    # 最长超时时间为10s
    wait = WebDriverWait(driver, 10)

    # 访问示例页面
    driver.get("file:///Users/lyy/Documents/project/DevAuto/selenium_python/4/demo.html")

    # 检查frame'是否可用，如果可用则切换至该frame
    ff = wait.until(frame_to_be_available_and_switch_to_it((By.ID, "baidu")))

    # 打印结果, 可用则返回True
    print(ff)

    driver.quit()
