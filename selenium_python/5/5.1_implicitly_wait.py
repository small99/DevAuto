# -*- coding: utf-8 -*-

__author__ = "苦叶子"


from selenium import webdriver


if __name__ == "__main__":
    # 创建webdriver对象
    driver = webdriver.chrome()

    # 设置隐式等待, 时间可以自定，一般建议设置30s以内
    # 即webdriver最长等待超过30s，则抛出超时异常
    driver.implicitly_wait(30)

    # 这里一般可以正常访问
    driver.get("http://www.python.org")

    # 这里你要是没vpn翻墙，30s后抛出超时异常
    driver.get("http://www.google.com")

    driver.quit()
