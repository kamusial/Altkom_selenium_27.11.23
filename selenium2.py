from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import datetime
from selenium.common.exceptions import NoSuchElementException

def make_screenshot(driver):
    teraz = datetime.datetime.now()
    file_name = teraz.strftime('screenshot%d-%M-%S.png')
    driver.get_screenshot_as_file(file_name)

if __name__ == '__main__':
    print('PLIK 2')
    driver = webdriver.Chrome()
    driver.get('https://www.saucedemo.com/')
    print('Nazwa strony', driver.title)
    time.sleep(3)

    try:
        username_field = driver.find_element(By.ID, 'user-name')
    except NoSuchElementException:
        make_screenshot(driver)
        raise

    username_field.clear()
    username_field.send_keys('standard_user')

    password_field = driver.find_element('xpath', '//*[@id="password"]')
    password_field.clear()
    password_field.send_keys('secret_sauce')

    login_button = driver.find_element('name', 'login-button')
    if not login_button.get_attribute('disabled'):
        login_button.click()

    make_screenshot(driver)
    driver.quit()
