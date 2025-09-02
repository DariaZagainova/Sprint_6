import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from locators.header_components_locators import HeaderComponentsLocator
from selenium.webdriver.support import expected_conditions as EC
from curl import Urls
from locators.main_page_locators import MainPageLocator
from pages.header_component import HeaderComponent

# Открывает браузер Mozilla Firefox, разворачивает окно на максимум, открывает главую страницу, закрывает окно после теста
@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(Urls.MAIN_PAGE)
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(MainPageLocator.MAIN_PAGE_WORK_AREA))
    yield driver
    driver.quit()

# Переходит на страницу заказа
@pytest.fixture
def go_to_order_page(driver):
    header = HeaderComponent(driver)
    header.click_order_button_header()
    WebDriverWait(driver, 10).until(EC.url_to_be(Urls.ORDER_PAGE))
    return driver