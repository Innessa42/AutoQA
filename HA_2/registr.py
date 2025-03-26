from selenium import webdriver
from selenium.webdriver.common.by import By
import time

webdriver = webdriver.Chrome()
webdriver.get("https://itcareerhub.de/ru")

link = webdriver.find_element(By.LINK_TEXT, "Способы оплаты")
link.click()
time.sleep(1)
webdriver.save_screenshot("link_image.png")

time.sleep(3)
