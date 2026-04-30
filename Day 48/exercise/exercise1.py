from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# Navigate to Wikipedia
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# Hone in on anchor tag using CSS Selectors
article_count = driver.find_elements(By.CSS_SELECTOR, '#articlecount a[title="Special:Statistics"]')
active_editors = article_count[0]
articles_total = article_count[1]
# articles_total.click()

#Find element by Link Text
all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

# Find the "Search" <input> by Name
search_bar = driver.find_element(By.NAME, "search")

# Sending keyboard input to Selenium
search_bar.send_keys("Python", Keys.ENTER)
# search_bar.send_keys(Keys.ENTER)

