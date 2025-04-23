import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
import pytest


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_ha5_1(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/iframes.html")

    obj_iframe = driver.find_element(By.ID, 'my-iframe')

    driver.switch_to.frame(obj_iframe)

    obj_text = driver.find_element(By.XPATH,
                                   '//*[contains(normalize-space(text()), "semper posuere integer et senectus justo curabitur.")]')
    assert obj_text.is_displayed()


def test_ha5_2(driver):
    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
    wait = WebDriverWait(driver, 2)
    accept_cookies_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[.="Consent"]')))
    accept_cookies_button.click()

    obj_iframe = driver.find_element(By.CSS_SELECTOR, "iframe.demo-frame")
    driver.switch_to.frame(obj_iframe)

    source_draggable = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'ui-draggable-handle')))
    target_droppable = driver.find_element(By.ID, 'trash')

    action = ActionChains(driver)
    action.drag_and_drop(source_draggable, target_droppable).perform()

    time.sleep(0.5)
    source_draggable_ul = driver.find_element(By.ID, "gallery")
    source_draggables_li = source_draggable_ul.find_elements(By.TAG_NAME, "li")

    assert len(source_draggables_li) == 3, "Не удалось переместить объект"

    target_droppables = driver.find_element(By.ID, 'trash')
    target_droppables_li = target_droppables.find_elements(By.TAG_NAME, "li")
    assert len(target_droppables_li) == 1, "В корзине нет объектов"

























#import pytest
#from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.action_chains import ActionChains
#from webdriver_manager.chrome import ChromeDriverManager
#import time
#
#
#@pytest.fixture
#def driver():
#    service = Service(ChromeDriverManager().install())
#    options = webdriver.ChromeOptions()
#    options.add_argument("--headless")  # Запуск без интерфейса браузера
#    driver = webdriver.Chrome(service=service, options=options)
#    driver.implicitly_wait(10)  # Ожидание элементов
#    yield driver
#    driver.quit()
#
#
#def test_itcareerhub_main_page(driver):
#    url = "https://itcareerhub.de/ru"
#    driver.get(url)
#
#    # Проверяем наличие логотипа
#    assert driver.find_element(By.CLASS_NAME, "header-logo"), "Логотип не найден"
#
#    # Проверяем наличие ссылок в меню
#    menu_links = {
#        "Программы": "//a[text()='Программы']",
#        "Способы оплаты": "//a[text()='Способы оплаты']",
#        "Новости": "//a[text()='Новости']",
#        "О нас": "//a[text()='О нас']",
#        "Отзывы": "//a[text()='Отзывы']"
#    }
#
#    for name, xpath in menu_links.items():
#        assert driver.find_element(By.XPATH, xpath), f"Ссылка '{name}' не найдена"
#
#    # Проверяем кнопки переключения языка
#    assert driver.find_element(By.XPATH, "//a[contains(@href, '/ru')]")
#    assert driver.find_element(By.XPATH, "//a[contains(@href, '/de')]")
#
#    # Клик по иконке с телефонной трубкой
#    phone_icon = driver.find_element(By.CLASS_NAME, "phone-icon")  # Уточните класс или селектор
#    phone_icon.click()
#
#    # Проверяем, что появилось нужное сообщение
#    message_xpath = "//*[contains(text(), 'Если вы не дозвонились, заполните форму на сайте. Мы свяжемся с вами')]"
#    assert driver.find_element(By.XPATH, message_xpath), "Сообщение о связи не найдено"
#
#
#def test_text_input_change(driver):
#    url = "http://uitestingplayground.com/textinput"
#    driver.get(url)
#
#    input_field = driver.find_element(By.ID, "newButtonName")
#    button = driver.find_element(By.ID, "updatingButton")
#
#    input_field.send_keys("ITCH")
#    button.click()
#
#    assert button.text == "ITCH", "Текст кнопки не изменился"
#
#
#def test_image_loading(driver):
#    url = "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
#    driver.get(url)
#
#    time.sleep(5)  # Ждем загрузки изображений
#
#    images = driver.find_elements(By.TAG_NAME, "img")
#    assert len(images) >= 3, "На странице меньше трех изображений"
#
#    third_image_alt = images[2].get_attribute("alt")
#    assert third_image_alt == "award", "Атрибут alt третьего изображения не равен 'award'"
#
#
#def test_iframe_text(driver):
#    url = "https://bonigarcia.dev/selenium-webdriver-java/iframes.html"
#    driver.get(url)
#
#    # Найти iframe и переключиться в него
#    iframe = driver.find_element(By.TAG_NAME, "iframe")
#    driver.switch_to.frame(iframe)
#
#    # Проверить наличие текста в iframe
#    text_element = driver.find_element(By.XPATH,
#                                       "//*[contains(text(), 'semper posuere integer et senectus justo curabitur.')]")
#    assert text_element.is_displayed(), "Текст не найден в iframe"
#
#    # Вернуться в основной контекст
#    driver.switch_to.default_content()
#
#
#def test_drag_and_drop(driver):
#    url = "https://www.globalsqa.com/demo-site/draganddrop/"
#    driver.get(url)
#
#    # Переключиться в iframe, если необходимо
#    driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))
#
#    # Найти изображение и корзину
#    image = driver.find_element(By.XPATH, "//ul[@id='gallery']/li[1]/img")
#    trash = driver.find_element(By.ID, "trash")
#
#    # Выполнить drag and drop
#    actions = ActionChains(driver)
#    actions.drag_and_drop(image, trash).perform()
#
#    # Проверить, что в корзине появилось одно изображение
#    trash_items = driver.find_elements(By.XPATH, "//div[@id='trash']/ul/li")
#    assert len(trash_items) == 1, "Изображение не появилось в корзине"
#
#    # Проверить, что в основной области осталось 3 изображения
#    remaining_images = driver.find_elements(By.XPATH, "//ul[@id='gallery']/li")
#    assert len(remaining_images) == 3, "В основной области не осталось 3 изображения"
#