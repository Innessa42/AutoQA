import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver

    driver.quit()


def test_itcareerhub_main_page(driver):
    url = "https://itcareerhub.de/ru"
    driver.get(url)

    # Проверяем наличие логотипа
    element = driver.find_element(By.CLASS_NAME, "tn-elem__7178437221710153310155")
    assert element, "тест не прошел"

    # Проверяем наличие ссылок в меню


    menu_links = {
        "Программы": 'Программы',
        "Способы оплаты": 'Способы оплаты',
        "Новости": 'Новости',
        "О нас": 'О нас',
        "Отзывы": 'Отзывы',
        "de":"de",
        "ru":"ru",
    }

    for name, link in menu_links.items():
        assert driver.find_element(By.LINK_TEXT, link), f"Ссылка '{name}' не найдена"



#    # Клик по иконке с телефонной трубкой
    phone_icon = driver.find_element(By.CLASS_NAME, "tn-elem__7178437221710153310161")  # Уточните класс или селектор
    phone_icon.click()

    # Проверяем, что появилось нужное сообщение
    message_xpath = "//*[contains(text(), 'Если вы не дозвонились, заполните форму на сайте. Мы свяжемся с вами')]"
    assert  message_xpath, "Сообщение о связи не найдено"

