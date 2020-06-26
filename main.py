import time
from selenium import webdriver
driver = webdriver.Chrome ('chromedriver.exe')
driver.get('http://newtours.demoaut.com/')
time.sleep(2)
user_box = driver.find_element_by_name('userName')
pass_box = driver.find_element_by_name('password')
submit_button = driver.find_element_by_name('login')
user_box.send_keys('test')
pass_box.send_keys('test')
submit_button.click()
time.sleep(3)
link_registration_form = driver.find_element_by_link_text('registration form')
assert link_registration_form.text == 'registration form'
print ('pasé por aquí')
assert link_registration_form.tag_name == 'a'
driver.quit()
