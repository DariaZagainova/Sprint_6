import allure
from pages.header_component import HeaderComponent

@allure.sub_suite ('class TestLogoHeaderNavigationInOrderPage: Проверка логотипов в шапке страницы заказа.')
class TestLogoHeaderNavigationInOrderPage:

    @allure.title ('Переход на главную страницу по клику на логотип "Самокат"')
    def test_click_scooter_logo_navigates_to_main_page(self, go_to_order_page):
        header = HeaderComponent(go_to_order_page)
        header.click_scooter_logo()

        assert header.check_expected_url_is_main_page()

    @allure.title('Открытие главной страницы Яндекс Дзена в новой вкладке по клику на логотип "Яндекс"')
    def test_click_yandex_logo_opens_dzen_main_page_in_new_tab(self, go_to_order_page):
        header = HeaderComponent(go_to_order_page)
        header.switch_after_yandex_logo_click()

        assert header.check_expected_url_is_dzen()
