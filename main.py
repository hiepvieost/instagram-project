import selenium
from selenium import webdriver
from selenium.common.exceptions import  NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from time import sleep

chrome_drive_path =  "C:\development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_drive_path)

URL = "https://www.instagram.com/"
ID = "duyhieple9999"
PASSWORD = "jaja23456"


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_drive_path)
    def login(self):
        # accept cookies
        self.driver.get(URL)
        sleep(3)
        cookies = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/button[1]')
        cookies.click()
        # login
        id = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        id.send_keys(ID)
        password = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)
    def find_follower(self):
        sleep(5)
        self.driver.get("https://www.instagram.com/gordongram")

        sleep(2)
        followers = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        sleep(2)


        modal = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]')

        for i in range(10):

            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(2)
    def follow(self):
        list_follower = self.driver.find_elements_by_css_selector('li button')
        for _ in list_follower:
            try:
                _.click()
                sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


bot = InstaFollower()
bot.login()
bot.find_follower()
bot.follow()
