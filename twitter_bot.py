import time
import pickle
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import os.path


def load_cookies(driver):
    for cookie in pickle.load(open("TwitterCookies.pkl", "rb")):
        driver.add_cookie(cookie)


def save_cookies(driver):
    pickle.dump(driver.get_cookies(), open("TwitterCookies.pkl", "wb"))


# read login details from file
def account_info():
    with open("account_info.txt", "r") as file:
        info = file.read().split()
        email = info[0]
        password = info[1]
    file.close()
    return email, password


def login(driver, email, password):
    email_xpath = '/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input'
    password_xpath = '/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input'
    login_xpath = '/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div/span/span'
    time.sleep(3)
    driver.find_element_by_xpath(email_xpath).send_keys(email)
    time.sleep(0.5)
    driver.find_element_by_xpath(password_xpath).send_keys(password)
    time.sleep(0.5)
    driver.find_element_by_xpath(login_xpath).click()


def tweet_picture(author_name, picture_path):
    options = Options()
    options.add_argument("start-maximized")
    driver = webdriver.Firefox(options=options)
    driver.get("https://twitter.com/login")

    #   check is user login before
    if os.path.isfile('TwitterCookies.pkl'):
        time.sleep(1)
        load_cookies(driver)
    else:
        email, password = account_info()
        login(driver, email, password)
        save_cookies(driver)

    #   xpath's for sharing tweets
    tweet_xpath = '/html/body/div/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div'
    message_xpath = '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[' \
                    '1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[' \
                    '2]/div '
    media_xpath = '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[4]/div/div/div[1]/input'
    post_xpath = '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[' \
                 '1]/div/div/div/div/div[2]/div[4]/div/div/div[2]/div[4]/div/span/span '

    #   sharing tweet steps
    time.sleep(4)
    driver.find_element_by_xpath(tweet_xpath).click()
    time.sleep(1)
    driver.find_element_by_xpath(message_xpath).send_keys(f"Author: {author_name}")
    time.sleep(1)
    file_upload_button = driver.find_element_by_xpath(media_xpath)
    file_upload_button.send_keys(picture_path)
    time.sleep(2)
    driver.find_element_by_xpath(post_xpath).click()
