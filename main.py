import os.path
import random
import time

import urllib.request
import requests
from bs4 import BeautifulSoup

import twitter_bot as tb

IS_RUNNING_ON_SERVER = False

#   constants
SLEEP_TIME = 86400  # a day to second
NUMBER_OF_PICTURES = 999
NOT_EXIST_KEYWORD = "Image does not"
FILE_NAME = "test.png"


def get_random_picture():
    id_ = random.randint(0, NUMBER_OF_PICTURES)
    random_url = f"https://picsum.photos/id/{id_}/info"
    html_text = requests.get(random_url).text
    soup = BeautifulSoup(html_text, "lxml").text
    return soup


def get_picture_and_author(info):
    """
    :type info: string
    """
    characters = ['"', '}', '{']
    for char in characters:
        info = info.replace(char, '')

    info = info.split(',')

    return info[1].split(':')[1], info[5].split('url:')[1]


def run():
    soup = get_random_picture()
    while NOT_EXIST_KEYWORD in soup:
        soup = get_random_picture()
    author, download_url = get_picture_and_author(soup)
    download_image(download_url)
    file_path = os.getcwd() + '\\' + FILE_NAME
    tb.tweet_picture(author, file_path)


#   if need to download and upload picture from local
def download_image(download_url):
    urllib.request.urlretrieve(download_url, FILE_NAME)


def run_in_server():
    while True:
        run()
        print("WAITING FOR A DAY ...")
        time.sleep(SLEEP_TIME)


if __name__ == "__main__":
    if IS_RUNNING_ON_SERVER:
        run_in_server()
    else:
        run()
