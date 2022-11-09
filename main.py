from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "C:\chromedriver_win32\chromedriver.exe"

service = Service(chrome_driver_path)

PASSWORD_XPATH = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input'

test = "Hi, this is written by a Python bot"
TWITTER_USERNAME = "jackcinar"
TWITTER_EMAIL = "cinarjack@gmail.com"
TWITTER_PASSWORD = "sananebe12345"

class InterSpeedTwitterBot:

    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(service=driver_path)
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(3)
        go_button = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go_button.click()

        time.sleep(50)
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/")
        time.sleep(2)
        login = self.driver.find_element(By.XPATH,
            '//*[@id="layers"]/div/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]/a')
        time.sleep(2)
        login.click()
        time.sleep(2)
        email = self.driver.find_element(By.XPATH,
            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')

        time.sleep(2)
        email.send_keys(TWITTER_USERNAME)
        time.sleep(2)
        email.send_keys(Keys.ENTER)
        time.sleep(2)
        password = self.driver.find_element(By.XPATH,
            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(TWITTER_PASSWORD)
        time.sleep(2)
        password.send_keys(Keys.ENTER)
        time.sleep(5)

        tweet = self.driver.find_element(By.XPATH,
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        tweet.send_keys(f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for more?")
        time.sleep(5)
        tweet_button = self.driver.find_element(By.XPATH,
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div/div/span/span')
        tweet_button.click()
        time.sleep(7)


bot = InterSpeedTwitterBot(service)
bot.get_internet_speed()
bot.tweet_at_provider()

