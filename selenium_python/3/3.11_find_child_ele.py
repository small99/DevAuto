# -*- coding: utf-8 -*-

__author__ = "苦叶子"


from selenium import webdriver


if __name__ == "__main__":

    driver = webdriver.Chrome()
    driver.implicitly_wait(3)

    driver.get("http://www.python.org")

    ele = driver.find_element_by_tag_name("fieldset").find_element_by_name("q")
    print(ele)

    driver.quit()
