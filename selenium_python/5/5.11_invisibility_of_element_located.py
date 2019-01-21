# -*- coding: utf-8 -*-

__author__ = "苦叶子"

from selenium import webdriver

# 导入WebDriverWait类
from selenium.webdriver.support.ui import WebDriverWait

# 导入定位方式
from selenium.webdriver.common.by import By

# 导入
from selenium.webdriver.support.expected_conditions import visibility_of_element_located


if __name__ == "__main__":
    driver = webdriver.Chrome()

    # 构建WebDriverWait对象
    # 最长超时时间为10s
    wait = WebDriverWait(driver, 10)

    # 访问示例页面
    driver.get("file:///Users/lyy/Documents/project/DevAuto/selenium_python/4/demo.html")

    # 检查一个存在并可见的input元素
    alert = wait.until(visibility_of_element_located((By.ID, "alert_id")))

    # 打印结果,
    print(alert)

    # 检查一个存在并不可见的input元素， 返回False或抛出异常
    v = wait.until(visibility_of_element_located((By.ID, "visibility_id")))

    # 打印结果
    print(v)

    driver.quit()
