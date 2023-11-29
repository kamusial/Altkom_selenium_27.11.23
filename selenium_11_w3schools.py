from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.w3schools.com/")
time.sleep(1)
# accept = driver.find_element(By.ID, 'accept-choices')
# accept.click()
driver.find_element(By.ID, 'accept-choices').click()
time.sleep(1)
# menu = driver.find_element(By.ID, 'navbtn_tutorials')
# menu.click()
# time.sleep(2)
menu = driver.find_element('id', 'navbtn_tutorials')
HTMLtutorial = driver.find_element(By.XPATH, '//*[@id="tutorials_html_css_links_list"]/div[1]/a[1]')



driver.quit()