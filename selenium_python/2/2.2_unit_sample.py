# -*- coding: utf-8 -*-

__author__ = "苦叶子"


from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


import unittest


class PythonSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_python_search(self):
        driver = self.driver
        driver.get("http://www.python.org")

        assert "Python" in driver.title

        ele = driver.find_element_by_name("q")

        ele.clear()

        ele.send_keys("pycon")

        ele.send_keys(Keys.RETURN)

        assert "No results found." not in driver.page_source

    def tearDown(self):

        sleep(5)

        self.driver.close()


if __name__ == "__main__":

    unittest.main()
