import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys

class PageIndex:
    def __init__(self, myDriver):
        self.driver = myDriver
        #self.user_box = self.driver.find_element_by_name('userName')
        #self.pass_box = self.driver.find_element_by_name('password')
        #self.register_link = self.driver.find_element_by_link_text('REGISTER')
        #self.submit_button = self.driver.find_element_by_name('login')
        #haciendo lo siguiente, le paso la responsabilidad de buscar el elemento al metodo
        self.user_box =(By.NAME, 'userName')
        self.pass_box =(By.NAME, 'password')
        self.register_link =(By.LINK_TEXT, 'REGISTER')
        self.submit_button =(By.NAME, 'login')

    def click_register (self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(*self.register_link).click()

    def login (self, user_name, password):
        self.driver.implicitly_wait(5)
        self.driver.find_element(*self.user_box).send_keys(user_name)
        self.driver.find_element(*self.pass_box).send_keys(password)
        try:
            submit = WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(self.submit_button))
        except:
            print('Element is not clickable')
        self.driver.find_element(*self.submit_button).click()

    def login_by_tab(self, user_name, password):
        self.driver.find_element(*self.user_box).send_keys(user_name+Keys.TAB+password+Keys.TAB+Keys.ENTER)

