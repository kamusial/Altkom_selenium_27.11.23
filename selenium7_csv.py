from selenium import webdriver
from selenium4_POM import LoginPage
from selenium2 import make_screenshot
from selenium.webdriver.common.by import By
from time import sleep
import pytest

path = r'C:\Users\Student\Desktop\ndane.csv'
path = 'C:\\Users\\Student\\Desktop\\ndane.csv'
mode = 'r'
with open(path, mode) as plik1:
    content = plik1.readlines()
print(content)

for i in range(len(content)):
    content[i] = content[i].split(',')
print(content)

print(content[4])   # linia
print(content[4][2])   # element
print(content[4][2][2])   # znak
print(content[4][2][2:9:2])    # konkretne znaki
print(content[4][2][::-1])
print(content[4][2][17:2:-3])
print(content[4][2][3:7])


#
# test_data = [
#     ('standard_user', 'secret_sauce', 'https://www.saucedemo.com/inventory.html'),
#     ('locked_out_user', 'secret_sauce', 'https://www.saucedemo.com/'),
#     ('problem_user', 'secret_sauce', 'https://www.saucedemo.com/inventory.html'),
#     ('performance_glitch_user', 'secret_sauce', 'https://www.saucedemo.com/inventory.html')
# ]
#
#
# @pytest.mark.parametrize('user, password, url', test_data)
# # @pytest.mark.skip(reason="bo tak")
# @pytest.mark.skipif(len('piesek') == 6, reason="bo tak")
# def test_login_page(user, password, url):
#     driver = webdriver.Chrome()
#     page = LoginPage(driver)
#     page.open()
#     page.print_page_info()
#     page.enter_username(user)
#     page.enter_password(password)
#     page.click_login()
# #    sleep(1)
#     try:
#         assert driver.current_url == url, make_screenshot(driver)
#     except AssertionError:
#         print('Assercja nie przeszła')
#         raise
#     else:
#         print('assercja przeszła')
#     finally:
#         print('Po asercji')
#         driver.quit()
#
# @pytest.mark.xfail
# def test_default():
#     assert 3 == 4
#
# @pytest.mark.xfail
# def test_default2():
#     assert 3 == 4