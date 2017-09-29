#! python3
# 使用火狐浏览器登录新浪免费邮箱

# Import modules
from selenium import webdriver

# Open a browser.
browser = webdriver.Firefox()

# Open the login page.
browser.get('https://mail.sina.com.cn')

# Get username and password elements.
usernameElem = browser.find_element_by_id('freename')
usernameElem.send_keys('YOUR_NAME@sina.cn')
passwdElem = browser.find_element_by_id('freepassword')
passwdElem.send_keys('YOUR_PASSWD')


# Login  Email
submitElem = browser.find_element_by_class_name('loginBtn')
submitElem.click()


