# -*- coding: utf-8 -*-

__author__ = "苦叶子"


from selenium import webdriver
from selenium.webdriver import ActionChains


if __name__ == "__main__":
    driver = webdriver.Chrome()
    action_chains = ActionChains(driver)
    driver.get("http://www.python.org")

    # 获取About链接元素，并加入动作链
    About = driver.find_element_by_link_text("About")
    action_chains.move_to_element(About)
    action_chains.pause(2)

    # 执行动作链
    action_chains.perform()

    driver.quit()
