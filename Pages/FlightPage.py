from selenium import webdriver
import unittest
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class FlightPage:
    #constructor, puedo declarar todos los elementos de mi pag para que sea mantenible a futuro
    def __init__(self,myDriver):
        self.driver = myDriver
        #self.countryDropDown = Select(self.driver.find_element_by_name('country'))
        self.countryDropdown = (By.NAME, 'country')

    def select_country_by_index(self, index):
        #self.countryDropDown.select_by_index(index)
        Select(self.driver.find_element(*self.countryDropdown)).select_by_index(index)

    def select_country_by_value(self, value):
        #self.countryDropDown.select_by_value(value)
        Select(self.driver.find_element(*self.countryDropdown)).select_by_value(value)

    def select_country_by_name(self, name):
        #self.countryDropDown.select_by_visible_text(name)
        Select(self.driver.find_element(*self.countryDropdown)).select_by_visible_text(name)

    def verify_country(self, country):
        tc = unittest.TestCase ('__init__')
        #tc.assertEqual(self.countryDropDown.first_selected_option.text.strip(), country)
        tc.assertEqual(Select(self.driver.find_element(*self.countryDropdown)).first_selected_option.text.strip(), country)

    def verify_not_country(self, country):
        tc = unittest.TestCase('__init__')
        tc.assertNotEqual(Select(self.driver.find_element(*self.countryDropdown)).first_selected_option.text.strip(), country)




    #self.assertEqual(countryDropDown.first_selected_option.text.strip(), country)
    # no me importa que haya, lo que me importa es que NO sea ITALIA
    # self.assertNotEqual(countryDropDown.first_selected_option.text.strip(), 'ITALY')
    # lo de adentro tiene que ser TRUE
    #self.assertTrue(countryDropDown.first_selected_option.text.strip() == 'CONGO')
    # lo de adentro tiene que ser FALSE
    #self.assertFalse(countryDropDown.first_selected_option.text.strip() == 'ARGENTINA')
    #self.assertFalse(countryDropDown.first_selected_option.text.strip() != 'CONGO')