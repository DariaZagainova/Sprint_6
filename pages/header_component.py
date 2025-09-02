import allure
from pages.base_page import BasePage
from locators.header_components_locators import HeaderComponentsLocator
from curl import Urls

class HeaderComponent(BasePage):
    
    @allure.step('Клик на логотип Самокат')
    def click_scooter_logo(self):
        self.click_on_element(HeaderComponentsLocator.SCOOTER_LOGO)

    @allure.step('Клик на логотип Яндекс')
    def click_yandex_logo(self):
        self.click_on_element(HeaderComponentsLocator.YANDEX_LOGO)

    @allure.step('Клик на кнопку "Заказать"')
    def click_order_button_header(self):
        self.click_on_element(HeaderComponentsLocator.ORDER_BUTTON_HEADER)

    @allure.step('Переход в новую вкладку после клика по логотипу "Яндекс"')
    def switch_after_yandex_logo_click(self):
        open_windows = self.get_open_windows()
        self.click_yandex_logo()
        self.switch_to_new_window(open_windows, Urls.YANDEX_REDIRECT)

    @allure.step('Проверяем, что текущий URL - главная страница Дзена')
    def check_expected_url_is_dzen(self):
        return self.get_current_url() == Urls.YANDEX_REDIRECT

    @allure.step('Проверяем, что текущий URL - главная страница')
    def check_expected_url_is_main_page(self):
        return self.get_current_url() == Urls.MAIN_PAGE        
    