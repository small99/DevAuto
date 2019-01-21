# -*- coding: utf-8 -*-

__author__ = "苦叶子"


from selenium import webdriver


if __name__ == "__main__":

    driver = webdriver.Chrome()
    driver.implicitly_wait(3)

    driver.get("http://www.python.org")

    # 通过xpath定位多个元素
    eles = driver.find_elements_by_xpath("//a")
    print(eles)

    # 通过tag name定位多个元素
    eles = driver.find_element_by_tag_name("li")
    print(eles)

    # 其他方法
    # driver.find_elements_by_id()
    # driver.find_elements_by_name()
    # driver.find_elements_by_class_name()
    # driver.find_elements_by_link_text()
    # driver.find_elements_by_partial_link_text()
    # driver.find_elements_by_css_selector()

    # 另外一种姿势
    # by 指定定位方式， value指定目标元素的定位参数
    # find_elements(by="id", value="id")

    driver.quit()
