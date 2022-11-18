from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('https://sso.teachable.com/secure/teachable_accounts/sign_in')

time.sleep(5)

element_teach = driver.find_element(By.NAME, "teachable_account[email]")