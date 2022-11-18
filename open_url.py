from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get('https://sso.teachable.com/secure/teachable_accounts/sign_in')

title = driver.title

time.sleep(3)

element_fill_user = driver.find_element(by=By.ID, value="teachable_account_email")
element_fill_user.send_keys(input("please enter you're username for teachable! "))

time.sleep(3)

element_fill_pass = driver.find_element(by=By.ID, value="teachable_account_password")
element_fill_pass.send_keys(input("Please enter you're password for teachable!"))
click_button = driver.find_element(by=By.NAME, value="commit")
click_button.click()

time.sleep(5)