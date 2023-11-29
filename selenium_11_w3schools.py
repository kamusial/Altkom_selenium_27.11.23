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
# menu.click()
HTMLtutorial = driver.find_element(By.XPATH, '//*[@id="tutorials_html_css_links_list"]/div[1]/a[1]')
# HTMLtutorial.click()
webdriver.ActionChains(driver).move_to_element(menu).click().move_to_element(HTMLtutorial).click().perform()
HTML_forms_attributes = driver.find_element(By.XPATH, '//*[@id="leftmenuinnerinner"]/a[41]')
HTML_forms_attributes.click()
tryityourself = driver.find_element(By.XPATH, '//*[@id="main"]/div[3]/a')
tryityourself.click()
time.sleep(1)

# runbtn = driver.find_element(By.ID, 'runbtn')
# runbtn.click()

currentWindowName = driver.current_window_handle
windowNames = driver.window_handles
print(currentWindowName)
print(windowNames)

for okno in windowNames:
    if okno != currentWindowName:
        driver.switch_to.window(okno)

# windowAdresses = []
# for karta in windowNames:
#     driver.switch_to.window(karta)
#     windowAdresses.append([driver.title, karta])
# print(windowAdresses)

driver.switch_to.frame(driver.find_element(By.ID, 'iframeResult'))
firstName = driver.find_element(By.ID, 'fname')
if firstName.is_enabled():
    firstName.clear()
    firstName.send_keys('Kamil')
else:
    print('nie da się kliknąć')
driver.close()
driver.quit()
