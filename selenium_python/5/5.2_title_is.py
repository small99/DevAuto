# -*- coding: utf-8 -*-

__author__ = "苦叶子"

from selenium import webdriver

# 导入WebDriverWait类
from selenium.webdriver.support.ui import WebDriverWait

# 导入title_is类
from selenium.webdriver.support.expected_conditions import title_is


if __name__ == "__main__":
    driver = webdriver.Chrome()

    # 构建WebDriverWait对象
    # 最长超时时间为10s
    wait = WebDriverWait(driver, 10)

    # 访问百度首页
    driver.get("http://www.baidu.com")

    # 百度首页的页面标题为：百度一下，你就知道
    # 不知道如何看一个页面的标题？那你该回去洗洗睡了
    # 使用title_is判断首页标准
    title = wait.until(title_is("百度一下，你就知道"))

    # 这里将打印出True，表示页面标题正确
    print(title)

    # 这里将等待10s，然后抛出timeout异常
    # 注意这里用的until_not与上面until的区别
    title = wait.until_not(title_is("百度一下，你就知道"))
    print(title)

    driver.quit()
