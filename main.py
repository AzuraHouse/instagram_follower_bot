from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time

CHROME_DRIVER_PATH = "Your Chrome driver path"
USERNAME = "Your username"
PASSWORD = "Your password"
SIMILAR_ACCOUNT = "Account name that you want to find"


class InstaFollower:

    def __init__(self):
        self.element_inside_popup = None
        self.search = None
        self.pw = None
        self.un = None
        self.CHROME_DRIVER_PATH = "Your Chrome driver path"
        self.service = Service(self.CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.get("https://www.instagram.com/")
        self.driver.maximize_window()

    def login(self):
        time.sleep(5)
        self.un = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        self.un.send_keys(USERNAME)
        self.pw = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        self.pw.send_keys(PASSWORD)
        self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').click()
        time.sleep(20)

    def find_followers(self):
        self.search = self.driver.find_element(By.XPATH,
                                               '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        self.search.send_keys(SIMILAR_ACCOUNT)
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/nav/div['
                                           '2]/div/div/div[2]/div[3]/div/div[2]/div/div['
                                           '1]/a/div').click()
        # Clicking on followers
        time.sleep(10)
        self.driver.find_element(By.XPATH, './/*[contains(text(), "followers")]/span').click()
        time.sleep(5)

    def follow(self):
        # Scrolling followers list
        self.element_inside_popup = self.driver.find_element(By.XPATH, "//div[@class='_aano']")
        while True:
            try:
                self.driver.find_element(By.XPATH, "//*[text()='Follow']").click()
                time.sleep(2)
            except ElementClickInterceptedException:
                pass
                # for h in range(10):
                #     self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", self.element_inside_popup)
                #     time.sleep(10)


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
