# Twitter Bot With Selenium
This bot is created with python and selenium. Tweets random picture and author of it. I used geckodriver for firefox webdriver.
- [geckodriver Repository](https://github.com/mozilla/geckodriver)

## Example Twitter Account
- [picassobot](https://twitter.com/picassobot1)

## Use
- You need to download webdriver for browser that you are using and you need to put exe file into your project folder.
- Used firefox webdriver in this project, if you want to use Chrome you need to make edits.
- You need to use account_info.txt file same as the example ->(email password) or (username password). There is only one blank line between email and password.
- If you want to host this bot in any server. You need to change variable IS_RUNNING_ON_SERVER (in main.py) to True.
- If you want to host local you need to automate with services of your operation system.
- Logging in only one time is enough, then program saves cookies and use cookies for opening twitter account. So twitter does not block account.

### Run
- python main.py

### Used External Libraries
- urllib
- requests
- BeautifulSoup
- selenium
