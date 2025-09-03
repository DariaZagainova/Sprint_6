import pytest
from selenium import webdriver
from curl import Urls
from pages.header_component import HeaderComponent

# Открывает браузер Mozilla Firefox, разворачивает окно на максимум, открывает главую страницу, закрывает окно после теста
@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(Urls.MAIN_PAGE)
    yield driver
    driver.quit()

# Переходит на страницу заказа
@pytest.fixture
def go_to_order_page(driver):
    header = HeaderComponent(driver)
    header.click_order_button_header()
    header.wait_open_order_page()
    return driver
