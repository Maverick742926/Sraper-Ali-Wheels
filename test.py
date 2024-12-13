import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lxml import html
from time import sleep

driver = webdriver.Chrome('./chromedriver.exe')

URL = 'https://www.aliexpress.com/'
driver.get(URL)
sleep(2)

closeAdd = driver.find_element(By.XPATH,"//img[@class='_24EHh']")
closeAdd.Click()

try:
    element = WebDriverWait(driver,10).until(
        EC.presence_of_all_elements_located((By.Xpath,"Close Add"))
    )
finally:
    driver.quit()


