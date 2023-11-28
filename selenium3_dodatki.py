from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as excon
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium2 import *

def wait_for_id(element_id):
    timeout = 5
    timeout_message = (f'Element {element_id} nie pojawil sie w czasie {timeout} s.')
    lokalizator = (By.ID, element_id)
    znaleziono = excon.visibility_of_element_located(lokalizator)
    oczekiwator = WebDriverWait(driver, timeout)
    return oczekiwator.until(znaleziono, timeout_message)

print('PLIK 3')
driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')
print('Nazwa strony', driver.title)

try:
    login_button = wait_for_id('login-buttonN')
except TimeoutException:
    print('Nie znaleziono')
    raise
else:
    print('Znaleziono')
finally:
    make_screenshot(driver)
    print('Zamykam przeglądarke')
    driver.quit()