from selenium import webdriver
from selenium4_POM import LoginPage
from selenium2 import make_screenshot
from selenium.webdriver.common.by import By
from time import sleep
import pytest

def test_login_page():
    driver = webdriver.Chrome()
    page = LoginPage(driver)
    page.open()
    page.print_page_info()
    page.enter_username('standard_userX')
    page.enter_password('secret_sauce')
    page.click_login()
    sleep(1)
    page.print_page_info()
    try:
        assert page.get_current_url() == page.after_login_url, make_screenshot(driver)
    except AssertionError:
        print('Assercja nie przeszła')
        raise
    else:
        print('assercja przeszła')
    finally:
        print('Po asercji')
        driver.quit()