from selenium.webdriver.common.by import By
from time import sleep
from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service
from mail import get_twitter_code
from utils import get_proxy_server_and_authentication, struct_proxy


def set_up_browser(proxy: str):
    options = webdriver.ChromeOptions()
    is_login_pass, proxy_server = get_proxy_server_and_authentication(proxy)
    options.add_argument(f'--proxy-server={proxy_server}')
    seleniumwire_options = None
    if is_login_pass:
        seleniumwire_options = {
            "proxy": struct_proxy(proxy)
        }

    options.add_argument('--lang=en')
    browser = webdriver.Chrome(service=Service(executable_path='chromedriver.exe'), options=options,
                               seleniumwire_options=seleniumwire_options)
    browser.get('https://twitter.com/i/flow/login')
    sleep(10)
    return browser


def enter_phone_num(browser, mail: str, mail_pass: str):
    code = get_twitter_code(mail, mail_pass)
    code_input = browser.find_element(By.CLASS_NAME, 'r-mk0yit')
    code_input = code_input.find_element(By.TAG_NAME, 'input')
    code_input.clear()
    code_input.send_keys(code)
    sleep(2)
    continue_button = browser.find_element(By.XPATH, "//*[contains(text(), 'Next')]")
    continue_button.click()
    sleep(6)


def enter_password(browser, password: str):
    password_input = browser.find_elements(By.TAG_NAME, 'input')
    password_input = password_input[-1]
    password_input.send_keys(password)
    sleep(2)
    enter_button = browser.find_element(By.XPATH, "//*[contains(text(), 'Log in')]//ancestor::span")
    enter_button.click()
    sleep(6)


def enter_username(browser, username: str):
    username_confirm_input = browser.find_element(By.TAG_NAME, 'input')
    username_confirm_input.clear()
    username_confirm_input.send_keys(username)
    sleep(2)
    enter_button = browser.find_element(By.XPATH, "//*[contains(text(), 'Next')]")
    enter_button.click()
    sleep(6)


def login(password: str, proxy: str, username: str = False, mail: str = False, mail_pass: str = False):
    browser = set_up_browser(proxy)
    enter_username(browser, username)
    enter_password(browser, password)
    sleep(3)
    if 'twitter.com/home' not in browser.current_url:
        enter_phone_num(browser, mail, mail_pass)
    cook = browser.get_cookie("auth_token")
    browser.quit()
    return cook["value"]
