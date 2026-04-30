#Incomplete

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

ACCOUNT_EMAIL = "mail123@mail.com"
ACCOUNT_PASSWORD = "something098765!"
# ACCOUNT_NAME = "Someone"
GYM_URL = "https://appbrewery.github.io/gym/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
driver.get(GYM_URL)

booked_count = 0
waitlist_count = 0
already_booked_count = 0

# -------------------------------------------------------------------

# def register():
#     register_btn = driver.find_element(By.ID, "toggle-login-register")
#     register_btn.click()
#     name_form = driver.find_element(By.ID, "name-input")
#     name_form.send_keys(ACCOUNT_NAME)
#     register_btn = driver.find_element(By.ID, "submit-button")
#     register_btn.click()

def login():
    login_btn = wait.until(ec.element_to_be_clickable((By.ID, "login-button")))
    login_btn.click()
    email_input = wait.until(ec.element_to_be_clickable((By.ID, "email-input")))
    email_input.clear()
    email_input.send_keys(ACCOUNT_EMAIL)
    password_input = wait.until(ec.element_to_be_clickable((By.ID, "password-input")))
    password_input.clear()
    password_input.send_keys(ACCOUNT_PASSWORD)
    submit_btn = driver.find_element(By.ID, "submit-button")
    submit_btn.click()





# -------------------------------------------------------------------

wait = WebDriverWait(driver, 2)

login()
wait.until(ec.presence_of_element_located((By.ID, "schedule-page")))

tuesday = driver.find_element(By.CSS_SELECTOR, '[id^="day-group-tue"]')
day = tuesday.find_element(By.CSS_SELECTOR, 'h2')
cards = tuesday.find_elements(By.CSS_SELECTOR, '[class*="ClassCard_cardHeader"]')

for card in cards:
    if "6:00 PM" in card.text:
        class_name = card.find_element(By.CSS_SELECTOR, "h3")
        button = card.find_element(By.TAG_NAME, "button")

        if button.text == "Booked":
            already_booked_count += 1
            print(f"✓ Already booked: {class_name.text} on {day.text}")
        elif button.text == "Waitlisted":
            already_booked_count += 1
            print(f"Already on waitlist: {class_name.text} on {day.text}")
        elif button.text == "Join Waitlist":
            button.click()
            waitlist_count += 1
            print(f"✓ Joined waitlist for: {class_name.text} on {day.text}")
        elif button.text == "Book Class":
            button.click()
            booked_count += 1
            print(f"✓ Booked: {class_name.text} on {day.text}")

print(f"--- BOOKING SUMMARY ---\n"
      f"Classes booked: {booked_count}\n"
      f"Waitlists joined: {waitlist_count}\n"
      f"Already booked/waitlisted: {already_booked_count}\n"
      f"Total Tuesday 6pm classes processes: {booked_count + waitlist_count + already_booked_count}")
