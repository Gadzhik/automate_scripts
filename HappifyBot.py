from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from auth_data import happify_username, happify_password
import time
import random
from selenium.common.exceptions import NoSuchElementException
import requests
import os


# создаем класс
class HappifyBot():

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.wdriver = webdriver.Chrome("/run/media/nnm/4E0ED8800ED8628F/Users/user/PycharmProjects/happify_reg/chromedriver/chromedriver")

    # создаем метод для закрытия браузера
    def browser_close(self):
        self.wdriver.close()
        self.wdriver.quit()

    # создаем метод для логина
    def login(self):
        wdriver = self.wdriver
        wdriver.get('https://stage.happify.com/login/')
        time.sleep(random.randrange(3,5))

        login_field = wdriver.find_element_by_id('email')
        login_field.clear()
        login_field.send_keys(happify_username)

        time.sleep(3)

        pass_field = wdriver.find_element_by_id('password')
        pass_field.clear()
        pass_field.send_keys(happify_password)

        time.sleep(3)

        pass_field.send_keys(Keys.ENTER)
        time.sleep(7)


mr_bot = HappifyBot(happify_username, happify_password)
mr_bot.login()
mr_bot.browser_close()









