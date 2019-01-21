# -*- coding: utf-8 -*-

__author__ = "苦叶子"

from selenium import webdriver

# 导入WebDriverWait类
from selenium.webdriver.support.ui import WebDriverWait

# 导入定位方式
from selenium.webdriver.common.by import By

# 导入
from selenium.webdriver.support.expected_conditions import presence_of_element_located,visibility_of


if __name__ == "__main__":
    driver = webdriver.Chrome()

    # 构建WebDriverWait对象
    # 最长超时时间为10s
    wait = WebDriverWait(driver, 10)

    # 访问百度首页
    driver.get("http://www.baidu.com")

    # 判断百度搜索框是否存在, 其id为kw
    kw_input = wait.until(presence_of_element_located((By.ID, 'kw')))
    kw = visibility_of(kw_input)

    # 这里将打印搜索框的WebElement对象
    print(kw)

    # 用name属性来判断
    wd_input = wait.until(presence_of_element_located((By.NAME, 'wd')))
    wd = visibility_of(wd_input)
    # 这里将打印搜索框的WebElement对象
    print(wd)

    # 看看判断隐藏的元素, 隐藏元素
    rn_input = wait.until(presence_of_element_located((By.NAME, 'rn')))
    rn = visibility_of(wd_input)
    # 这里将打印搜索框的WebElement对象
    print(rn)

    # 如果目标元素不可见，且width、height属性为0则抛出异常，大家可以自己试试

    driver.quit()
