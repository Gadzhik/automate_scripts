from selenium import webdriver
import time
import random
from reg_data import username, password, email, timestr
from selenium.webdriver.common.keys import Keys


# создаем класс
class HappifyBotRegister():

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        #self.wdriver = webdriver.Chrome("/run/media/nnm/4E0ED8800ED8628F/Users/user/PycharmProjects/happify_reg/chromedriver/chromedriver")
        self.wdriver = webdriver.Chrome("C:\\Users\\user\\PycharmProjects\\happify_reg\\chromedriver\\chromedriver.exe")


    # создаем метод для закрытия браузера
    def browser_close(self):
        self.wdriver.close()
        self.wdriver.quit()

    # создаем метод для логина
    def register(self):
        wdriver = self.wdriver
        wdriver.get('https://stage.happify.com/')
        time.sleep(random.randrange(3,5))

        get_started_btn = wdriver.find_element_by_xpath('/html/body/main/section[1]/div/button').click()
        time.sleep(3)

        get_started_today_btn = wdriver.find_element_by_xpath('//*[@id="watson-assessment-brain-screen"]/div/div[3]/div/button').click()
        time.sleep(3)

        answer_2 = wdriver.find_element_by_id('answer_2').click()
        time.sleep(3)

        answer_5 = wdriver.find_element_by_id('answer_5').click()
        time.sleep(2)

        answer_6 = wdriver.find_element_by_id('answer_6').click()
        time.sleep(3)

        button_next = wdriver.find_element_by_class_name('button').click()
        time.sleep(3)

        answer_retired = wdriver.find_element_by_id('answer_5').click()
        time.sleep(3)

        answer_no = wdriver.find_element_by_id('answer_2').click()
        time.sleep(2)

        answer_18_yers = wdriver.find_element_by_id('answer_5').click()
        time.sleep(2)

        btn_next = wdriver.find_element_by_class_name('button').click()
        time.sleep(2)

        very_much = wdriver.find_element_by_id('answer_3').click()
        time.sleep(2)

        some_what = wdriver.find_element_by_id('answer_3').click()
        time.sleep(2)

        a_little = wdriver.find_element_by_id('answer_1').click()
        time.sleep(2)

        often_answ = wdriver.find_element_by_id('answer_3').click()
        time.sleep(2)

        not_interested_ans = wdriver.find_element_by_id('answer_1').click()
        time.sleep(2)

        btn_nxt = wdriver.find_element_by_class_name('button').click()
        time.sleep(7)

        #self.wdriver.find_element_by_css_selector('body')

        username_field = wdriver.find_element_by_xpath('//*[@id="signup_modal"]/div[2]/div/div/div[5]/form/div[1]/div/label/input')
        username_field.send_keys(username)
        time.sleep(2)

        email_field = wdriver.find_element_by_xpath('//*[@id="signup_modal"]/div[2]/div/div/div[5]/form/div[2]/div/label/input')
        email_field.send_keys(email)
        time.sleep(2)

        password_fiel = wdriver.find_element_by_xpath('//*[@id="signup_modal"]/div[2]/div/div/div[5]/form/div[3]/div/label/input')
        password_fiel.send_keys(password)
        time.sleep(2)

        confirm_passwd_field = wdriver.find_element_by_xpath('//*[@id="signup_modal"]/div[2]/div/div/div[5]/form/div[4]/div/label/input')
        confirm_passwd_field.send_keys(password)
        time.sleep(2)

        confirm_cech_box = wdriver.find_element_by_class_name('terms_box-label').click()
        time.sleep(2)

        continue_btn = wdriver.find_element_by_class_name('button').click()
        time.sleep(7)


mr_bot = HappifyBotRegister(username, email, password)
mr_bot.register()
mr_bot.browser_close()















































