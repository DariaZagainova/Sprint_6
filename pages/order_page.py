import allure
from locators.order_page_locators import OrderPageLocator
from pages.base_page import BasePage
from helpers import extract_day_and_month_from_date

class OrderPage(BasePage):

    @allure.step('Вводим имя: {name} в поле Имя ')
    def fill_name(self, name):
        self.send_keys_to_input(OrderPageLocator.NAME_INPUT, name)

    @allure.step('Вводим фамилию: {last_name} в поле Фамилия')
    def fill_last_name(self, last_name):
        self.send_keys_to_input(OrderPageLocator.LAST_NAME_INPUT, last_name)

    @allure.step('Вводим адрес: {address} в поле Адрес')
    def fill_address(self, address):
        self.send_keys_to_input(OrderPageLocator.ADDRESS_INPUT, address)

    @allure.step('Кликаем на поле выбора станции метро')
    def click_metro_station_input(self):
        self.click_on_element(OrderPageLocator.METRO_STATION_INPUT)

    @allure.step('Ожиданиие открытия списка станций метро')
    def wait_metro_station_dropdown(self):      
        self.wait_for_element(OrderPageLocator.METRO_DROPDOWN_LIST)

    @allure.step('Клик по станции метро: {metro_station}')
    def select_metro_station(self, metro_station):
        locator = OrderPageLocator.get_metro_option_locator(metro_station) 
        # self.wait_for_element(locator)
        self.scroll_to_element(locator)
        self.click_on_element(locator)

    @allure.step('Ожидание, что выбранная {metro_station} в плэйсхолдере')
    def wait_metro_station_in_placeholder(self, metro_station):
        locator = OrderPageLocator.get_metro_placeholder_locator(metro_station)
        self.wait_for_element(locator)
         
    @allure.step('Вводим телефон: {phone} в поле Телефон')
    def fill_phone(self, phone):
        self.send_keys_to_input(OrderPageLocator.PHONE_INPUT, phone)

    @allure.step('Заполняем форму регистрации c личными данными')
    def fill_order_form_personal_data(self, order_form_data):

        self.fill_name(order_form_data["name"])
        self.fill_last_name(order_form_data["last_name"])
        self.fill_address(order_form_data["address"])
        self.click_metro_station_input()
        self.wait_metro_station_dropdown()
        self.select_metro_station(order_form_data["metro_station"])
        self.fill_phone(order_form_data["phone"])

    @allure.step('Нажимаем кнопку "Далее" после заполнения формы заказа с личными данными')
    def click_button_next(self):
        self.click_on_element(OrderPageLocator.NEXT_BUTTON)

    @allure.step('Клик по полю "Когда привезти самокат"')
    def click_when_to_deviler_input(self):
        self.click_on_element(OrderPageLocator.WHEN_TO_DELIVER_INPUT)

    @allure.step('Ожиданиие открытия выпадающего календаря')
    def wait_datepicker_container(self):      
        self.wait_for_element(OrderPageLocator.DATEPICKER_CONTAINER)

    @allure.step('Клик по дате: "{date_order}"')
    def select_date_order(self, date_order):
        day, month = extract_day_and_month_from_date(date_order)
        locator = OrderPageLocator.get_calendar_day_locator(day)
        for _ in range(12):
            if month in self.get_text_element(OrderPageLocator.DATEPICKER_CURRENT_MONTH):
                self.click_on_element(locator)
                break
            else:
                self.click_on_element(OrderPageLocator.DATEPICKER_NEXT_MONTH_BUTTON)

    @allure.step('Проверяем, что "{date_order}" в плэйсхолдере')
    def check_date_order_in_placeholder(self, date_order):
        actual_value = self.get_value_element (OrderPageLocator.WHEN_TO_DELIVER_INPUT)
        return actual_value == date_order

    @allure.step('Клик по полю "Срок аренды"')
    def click_rental_term_dropdown(self):
        self.click_on_element(OrderPageLocator.RENTAL_TERM_DROPDOWN)

    @allure.step('Ожиданиие открытия списка со сроками аренды')
    def wait_rental_term_dropdown_menu(self):      
        self.wait_for_element(OrderPageLocator.RENTAL_TERM_DROPDOWN_MENU)

    @allure.step('Клик по сроку аренды: "{term_order}"')
    def select_rental_term_order(self, term_order):
        locator = OrderPageLocator.get_rental_term_option_locator(term_order) 
        self.scroll_to_element(locator)
        self.click_on_element(locator)

    @allure.step('Проверяем, что "{term_order}" в плэйсхолдере')
    def check_rental_term_order_in_placeholder(self, term_order):
        actual_value = self.get_text_element (OrderPageLocator.RENTAL_TERM_DROPDOWN)
        return actual_value == term_order
        
    @allure.step('Клик по цвету самоката: "{colour}"')
    def select_scooter_colour(self, colour):
        locator = OrderPageLocator.get_colour_checkbox_locator(colour)
        self.click_on_element(locator)

    @allure.step('Проверяем, что чекбокс: "{colour}" выбран')
    def check_checkbox__scooter_colour_is_selected(self, colour):
        locator = OrderPageLocator.get_colour_checkbox_locator(colour)
        return self.is_element_selected(locator)

    @allure.step('Клик на кнопку "Заказать" в центре страницы заказа')
    def click_order_button_middle(self):
        self.click_on_element(OrderPageLocator.ORDER_BUTTON_MIDDLE)

    @allure.step('Проверяем, что окно "Хотите оформить заказ" открыто')
    def check_order_window_popup_is_open(self):
        self.wait_for_element(OrderPageLocator.ORDER_MODAL_HEADER_POPUP)

    @allure.step('Заполняем форму регистрации c даннымии заказа')
    def fill_order_form_order_data(self, order_form_data):

        self.click_when_to_deviler_input()
        self.wait_datepicker_container()
        self.select_date_order(order_form_data["date_order"])
        self.check_date_order_in_placeholder(order_form_data["date_order"])
        self.click_rental_term_dropdown()
        self.wait_rental_term_dropdown_menu()
        self.select_rental_term_order(order_form_data["term_order"])
        self.check_rental_term_order_in_placeholder(order_form_data["term_order"])
        self.select_scooter_colour(order_form_data["colour"])
        self.check_checkbox__scooter_colour_is_selected(order_form_data["colour"])
        
    @allure.step('Клик на кнопку "Да" в всплывающем окне Хотите оформить заказ')
    def click_popup_yes_button(self):
        self.click_on_element(OrderPageLocator.ORDER_POPUP_YES_BUTTON)

    @allure.step('Проверяем, что появилось окно "Заказ оформлен"')
    def check_success_order_window_is_open(self):
        return self.wait_for_element(OrderPageLocator.ORDER_SUCCESS_ORDER_POPUP_HEADER)
    