import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


zillow_url = "https://appbrewery.github.io/Zillow-Clone/"
questions_form = "https://docs.google.com/forms/d/e/1FAIpQLScP2FqRRd9wI8LfAiTlS-jFDOcJmkXy-QK45AL53iHvntbc6Q/viewform"

response = requests.get(zillow_url)
soup = BeautifulSoup(response.content, 'html.parser')

property_address_list = []
property_price_list = []
property_url_list = []

listings = soup.find_all('article', {"data-test": "property-card"})

for data in listings:
    url = data.find(attrs={'data-test': 'property-card-link'})
    property_url_list.append(url['href'])
    addr = data.find(attrs={'data-test': 'property-card-addr'})
    property_address_list.append(addr.get_text().strip("\n ").replace(" | ", ", "))
    price = data.find(attrs={'data-test': 'property-card-price'})
    property_price_list.append(price.get_text().strip("+ /mo 1 bd"))

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

short_wait = WebDriverWait(driver, 5)

driver.get(questions_form)

for i in range(len(property_url_list)):
    time.sleep(0.5)
    # questions_block = short_wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "[role='list']")))
    inputs = short_wait.until(ec.presence_of_all_elements_located((By.CSS_SELECTOR, "[role='list'] input")))
    inputs[0].send_keys(property_address_list[i])
    inputs[1].send_keys(property_price_list[i])
    inputs[2].send_keys(property_url_list[i])
    driver.find_element(By.CSS_SELECTOR, "[aria-label='Submit']").click()
    time.sleep(0.5)
    short_wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "div a[href]"))).click()
