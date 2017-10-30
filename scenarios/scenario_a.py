'''
Created on Sep 28, 2017

@author: labinav
'''
# -*- coding: utf8 -*-
 
import unittest
 
from selenium import webdriver
from ddt import ddt, data, unpack
 
from library.GetData import get_csv_data
 
 
@ddt
class TestScenarioA(unittest.TestCase):
    """ inheriting the TestCase class"""
 
    @classmethod
    def setUpClass(cls):
        """test preparation"""
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(3)
        cls.driver.set_window_size(450, 500)
 
    @data(*get_csv_data('./data/scenario_a.csv'))
    @unpack
    def test_search(self, target_url, elem_name, search_value):
        """test case for scenario a"""
        driver = self.driver
        driver.get(target_url)
 
        btn_elem = driver.find_element_by_id('search-toggle')
        btn_elem.click()
 
        input_elem = driver.find_element_by_name(elem_name)
        input_elem.clear()
        input_elem.send_keys(search_value)
        input_elem.submit()
 
    @classmethod
    def tearDownClass(cls):
        """clean up"""
        cls.driver.close()
