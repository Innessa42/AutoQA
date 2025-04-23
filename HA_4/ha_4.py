#Тестируемый сайт:
#http://uitestingplayground.com/textinput
#Шаги теста:
#Перейдите на сайт Text Input.
#Введите в поле ввода текст "ITCH".
#Нажмите на синюю кнопку.
#Проверьте, что текст кнопки изменился на "ITCH".
# Проверяем, что появилось нужное сообщение
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver

    driver.quit()

#message_xpath = "//*[contains(text(), 'Если вы не дозвонились, заполните форму на сайте. Мы свяжемся с вами')]"
#assert driver.find_element(By.XPATH, message_xpath), "Сообщение о связи не найдено"


def test_text_input_change(driver):
    url = "http://uitestingplayground.com/textinput"
    driver.get(url)

    input_field = driver.find_element(By.ID, "newButtonName")
    button = driver.find_element(By.ID, "updatingButton")

    input_field.send_keys("ITCH")
    button.click()

    assert button.text == "ITCH", "Текст кнопки не изменился"


def test_image_loading(driver):
    url = "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
    driver.get(url)

    time.sleep(10)  # Ждем загрузки изображений
    element_div = driver.find_element(By.ID, "image-container")


    images =  element_div.find_elements(By.TAG_NAME, "img")
    assert len(images) >= 3, "На странице меньше трех изображений"

    third_image_alt = images[2].get_attribute("alt")
    assert third_image_alt == "award", "Атрибут alt третьего изображения не равен 'award'"


##############################
#def test_button_new_name(driver):
#    driver.get("http://uitestingplayground.com/textinput")
#    element_new_button_name = driver.find_element(By.ID, "newButtonName")
#    element_new_button_name.send_keys("ITCH")
#    element_button_set_name = driver.find_element(By.ID, "updatingButton")
#    element_button_set_name.click()
#    assert element_button_set_name.text == "ITCH", "Текст не изменился"
#
#def test_image_upload(driver):
#    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
#    time.sleep(10)
#
#    element_div = driver.find_element(By.ID, "image-container")
#
#    elements_img = element_div.find_elements(By.TAG_NAME, "img")
#
#    assert elements_img[2].get_attribute("alt") == "award"