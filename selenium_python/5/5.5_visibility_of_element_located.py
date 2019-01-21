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

    # 访问百度首页
    driver.get("http://www.baidu.com")

    # 判断百度搜索框是否存在, 其id为kw
    kw = wait.until(visibility_of_element_located((By.ID, "kw")))
    print(kw)

    # 用name属性来判断
    wd = wait.until(visibility_of_element_located((By.NAME, "wd")))
    print(wd)

    # 看看判断隐藏的元素, 隐藏元素不可见，抛出异常
    rn = wait.until(visibility_of_element_located((By.NAME, "rn")))
    print(rn)

    driver.quit()
