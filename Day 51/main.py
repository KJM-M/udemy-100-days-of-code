import os
import time
import random
from dotenv import load_dotenv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc

load_dotenv()

PROMISED_DOWN = 10
PROMISED_UP = 10
TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")
TWITTER_USERNAME = os.getenv("TWITTER_USERNAME")

SPEED_TEST_URL = "https://www.speedtest.net/"
TWITTER_URL = "https://www.twitter.com/login"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = None
        self.download_speed = 0
        self.upload_speed = 0
        self.ping = 0
        self.init_driver()
        self.short_wait = WebDriverWait(self.driver, 5)
        self.long_wait = WebDriverWait(self.driver, 15)

    def init_driver(self):
        chrome_options = uc.ChromeOptions()
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_argument("--no-first-run")
        chrome_options.add_argument("--no-default-browser-check")
        chrome_options.add_argument("--deny-permission-prompts")

        self.driver = uc.Chrome(options=chrome_options, version_main=147, keep_alive=True)


    def get_internet_speed(self):
        self.driver.get(SPEED_TEST_URL)

        try: # Reject cookies
            self.short_wait.until(ec.element_to_be_clickable((By.ID, "onetrust-reject-all-handler"))).click()
        except TimeoutException:
            pass

        # ---------------- SPEEDTEST ----------------
        self.short_wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, ".start-button a"))).click()
        time.sleep(40) # Keksi parempi tapa

        result_container = self.short_wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "result-container-data")))
        self.download_speed = result_container.find_element(By.CSS_SELECTOR, ".download-speed").text
        self.upload_speed = result_container.find_element(By.CSS_SELECTOR, ".upload-speed").text

        result_details = self.short_wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "result-item-details")))
        self.ping = result_details.find_element(By.CSS_SELECTOR, ".ping-speed").text


    def tweet_at_provider(self):
        self.driver.get(TWITTER_URL)

        # ---------------- LOGIN TWITTER ----------------
        user_input = self.long_wait.until(ec.element_to_be_clickable((By.NAME, "text")))
        user_input.click()

        for char in TWITTER_EMAIL:
            time.sleep(random.uniform(0.05, 0.2))
            user_input.send_keys(char)

        self.driver.find_element(By.XPATH, "//button[.//span[text()='Next']]").click()

        self.short_wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "input")))

        if len(self.driver.find_elements(By.NAME, "text")) > 0:
            username_input = self.driver.find_element(By.NAME, "text")
            username_input.click()
            for char in TWITTER_USERNAME:
                time.sleep(random.uniform(0.05, 0.2))
                username_input.send_keys(char)
            self.driver.find_element(By.CSS_SELECTOR, "[data-testid='ocfEnterTextNextButton']").click()

        time.sleep(2)

        if len(self.driver.find_elements(By.NAME, "password")) > 0:
            password_input = self.driver.find_element(By.NAME, "password")
            password_input.click()
            for char in TWITTER_PASSWORD:
                time.sleep(random.uniform(0.05, 0.2))
                password_input.send_keys(char)
            self.driver.find_element(By.CSS_SELECTOR, "[data-testid='LoginForm_Login_Button']").click()

        # ---------------- TWEET ----------------
        time.sleep(10)

        tweet_box = self.long_wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "[role='textbox']")))
        tweet_box.click()
        tweet_box.send_keys(f"Hey Internet Provider, why is my internet speed:\n"
                            f"{self.download_speed}down/{self.upload_speed}up ({self.ping}ms)\n"
                            f"When i pay for {PROMISED_DOWN}down/{PROMISED_DOWN}up")
        self.short_wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='tweetButtonInline']"))).click()

        self.driver.quit()

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
