# -*- coding: utf-8 -*-

__author__ = "苦叶子"

from selenium import webdriver

# 导入WebDriverWait类
from selenium.webdriver.support.ui import WebDriverWait

# 导入定位方式
from selenium.webdriver.common.by import By

# 导入
from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located


if __name__ == "__main__":
    driver = webdriver.Chrome()

    # 构建WebDriverWait对象
    # 最长超时时间为10s
    wait = WebDriverWait(driver, 10)

    # 访问百度首页
    driver.get("http://www.baidu.com")

    # 判断是否存在至少一个input元素
    # 返回已经找到的元素的列表集
    kw = wait.until(presence_of_all_elements_located((By.XPATH, "//input")))
    print("===" * 10)
    print(kw)

    # 找一个不存在的元素试试
    # 抛出异常
    rn = wait.until(presence_of_all_elements_located((By.XPATH, "//input[@id='123']")))
    print("---" * 10)
    print(rn)

    driver.quit()
