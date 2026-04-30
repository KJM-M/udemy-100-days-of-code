from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = "https://secure-retreat-92358.herokuapp.com/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

# Find the first name, last name, and email fields
f_name = driver.find_element(By.NAME, 'fName')
l_name = driver.find_element(By.NAME, 'lName')
email = driver.find_element(By.NAME, 'email')

# Fill out the form
f_name.send_keys('FirstName')
l_name.send_keys('LastName')
email.send_keys('mail@mail.fi')


sign_up = driver.find_element(By.CSS_SELECTOR, 'form button')
sign_up.click()