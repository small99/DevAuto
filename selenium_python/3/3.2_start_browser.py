# -*- coding: utf-8 -*-

__author__ = "苦叶子"


from time import sleep
from selenium import webdriver


if __name__ == "__main__":
    # firefox
    driver = webdriver.Firefox()
    driver.get("http://www.python.org")
    sleep(1)
    driver.quit()

    # ie
    driver = webdriver.Ie()
    driver.get("http://www.python.org")
    sleep(1)
    driver.quit()

    # edge
    driver = webdriver.Edge()
    driver.get("http://www.python.org")
    sleep(1)
    driver.quit()

    # chrome
    driver = webdriver.Chrome()
    driver.get("http://www.python.org")
    sleep(1)
    driver.quit()

    # opera
    driver = webdriver.Opera()
    driver.get("http://www.python.org")
    sleep(1)
    driver.quit()

    # phantomjs
    driver = webdriver.PhantomJS()
    driver.get("http://www.python.org")
    sleep(1)
    driver.quit()

    # 其他
