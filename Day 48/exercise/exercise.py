from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create and configure the Chrome webdriver
driver = webdriver.Chrome(options=chrome_options)

# Python.org
driver.get("https://www.python.org/")

# Amazon's Instant Pot
# driver.get("https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")

# By.CLASS_NAME (uses amazon.com website)
# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is {price_dollar.text}.{price_cents.text}")

# Locatin strategies for a single element
# By.NAME
search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))

# By.ID
button = driver.find_element(By.ID, value="submit")
# print(button.size)

# By.CSS_SELECTOR
documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link.text)

# By.XPath
bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

# Finding multiple elements
tier_1 = driver.find_elements(By.CLASS_NAME, value="tier_1")

# Challenge: Print the event dates from python.org
event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

events = {}


for i in range(len(event_times)):
    events[i] = {
        "time": event_times[i].text,
        "name": event_names[i].text,
    }

print(events)




# driver.close()
driver.quit()