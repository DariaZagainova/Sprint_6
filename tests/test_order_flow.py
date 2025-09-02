import pytest
import allure
from pages.order_page import OrderPage
from pages.main_page import MainPageOrderButton
from locators.main_page_locators import MainPageLocator
from locators.header_components_locators import HeaderComponentsLocator
from curl import Urls
from data import order_form_data


@allure.sub_suite('class TestOrderFlow: Флоу позитивного сценария заказа самоката.')
class TestOrderFlow:

    @allure.title('Проверка появления окна “Заказ оформлен” после заполнения формы заказа через разные кнопки "Заказать" и наборы данных')
    @allure.description('Первый прогон теста: заход через кнопку "Заказать" в шапке главной страницы, используется первый набор данных. ' \
    'Второй прогон теста: заход через кнопку "Заказать" в середине главной страницы, используется второй набор данных. ' \
    'Проверяется, что после заполнения формы появляется окно "Заказ оформлен".')
    @pytest.mark.parametrize("entry_locator, order_form_data", 
    [
        (HeaderComponentsLocator.ORDER_BUTTON_HEADER, order_form_data[0]),
        (MainPageLocator.ORDER_BUTTON_MIDDLE, order_form_data[1]),
    ])
    def test_fill_order_form_1(self, driver, entry_locator, order_form_data):
        main_page = MainPageOrderButton(driver)
        main_page.click_order_button(entry_locator)

        order_page = OrderPage(driver)
        order_page.fill_order_form_personal_data(order_form_data)
        order_page.click_button_next()
        order_page.fill_order_form_order_data(order_form_data)
        order_page.click_order_button_middle()
        order_page.check_order_window_popup_is_open()
        order_page.click_popup_yes_button()

        assert order_page.check_success_order_window_is_open()
