from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get('https://sso.teachable.com/secure/teachable_accounts/sign_in')

title = driver.title

time.sleep(5)

element_teach = driver.find_element(By.NAME, "teachable_account[email]")