# -*- coding: utf-8 -*-

__author__ = "苦叶子"


from selenium import webdriver


if __name__ == "__main__":

    driver = webdriver.Chrome()
    driver.implicitly_wait(3)

    driver.get("http://www.python.org")

    # 通过正确xpath
    ele = driver.find_element_by_xpath("//input[@id='id-search-field']")
    print(ele)

    # 给错误xpath，看下定位到的结果是什么
    ele = driver.find_element_by_xpath("//input[@id='id-search-field-error']")
    print(ele)

    driver.quit()
