# -*- coding: utf-8 -*-

__author__ = "苦叶子"

from selenium import webdriver

# 导入WebDriverWait类
from selenium.webdriver.support.ui import WebDriverWait

# 导入定位方式
from selenium.webdriver.common.by import By

# 导入
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element


if __name__ == "__main__":
    driver = webdriver.Chrome()

    # 构建WebDriverWait对象
    # 最长超时时间为10s
    wait = WebDriverWait(driver, 10)

    # 访问百度首页
    driver.get("http://www.baidu.com")

    # 判断 新闻 文本是否在指定的链接元素中
    kw = wait.until(text_to_be_present_in_element((By.NAME, "tj_trnews"), "新闻"))

    # 打印出True
    print(kw)

    driver.quit()
