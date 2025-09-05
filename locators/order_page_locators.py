from selenium.webdriver.common.by import By
from data import colours

class OrderPageLocator:

    NAME_INPUT = (By.XPATH, '//input[@placeholder="* Имя"]') # Поле ввода Имя
    LAST_NAME_INPUT = (By.XPATH, '//input[@placeholder="* Фамилия"]') # Поле ввода Фамилия
    ADDRESS_INPUT = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]') # Поле ввода адреса
    METRO_STATION_INPUT = (By.XPATH, '//input[@placeholder="* Станция метро"]') # Поле с выпадающим список со станциями метро
    METRO_DROPDOWN_LIST = (By.CLASS_NAME, 'select-search__select') # Выпадающий список со станциями метро
    PHONE_INPUT = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]') # Поле ввода Телефон
    NEXT_BUTTON = (By.XPATH, '//button[text()="Далее"]') # Кнопка Далее
    WHEN_TO_DELIVER_INPUT = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]') # Поле с выпадающим календарем
    DATEPICKER_CONTAINER = (By.CLASS_NAME, 'react-datepicker__month-container') # Выпадающий календарь
    DATEPICKER_CURRENT_MONTH = (By.CLASS_NAME, 'react-datepicker__current-month')  # Текущий месяц в календаре
    DATEPICKER_NEXT_MONTH_BUTTON = (By.CLASS_NAME, 'react-datepicker__navigation--next')  # Кнопка перехода к следующему месяцу в календаре
    RENTAL_TERM_DROPDOWN = (By.CLASS_NAME, 'Dropdown-placeholder') # Поле с выпадающим списком срока аренды
    RENTAL_TERM_DROPDOWN_MENU = (By.CLASS_NAME, 'Dropdown-menu') # Выпадающий список срока аренды
    BLACK_SCOOTER_CHECKBOX = (By.ID, 'black') # Чекбокс "чёрный жемчуг" в блоке с выбором цвета самоката
    GREY_SCOOTER_CHECKBOX = (By.ID, 'grey') # Чекбокс "серая безысходность" в блоке с выбором цвета самоката
    ORDER_BUTTON_MIDDLE = (By.XPATH, '//button[contains(@class, "Button_Middle") and contains(text(), "Заказать")]') # Кнопка заказать в центре страницы
    ORDER_MODAL_HEADER_POPUP = (By.CLASS_NAME, 'Order_ModalHeader__3FDaJ') # Заголовок всплывающего окна Хотите оформить заказ?
    ORDER_POPUP_YES_BUTTON = (By.XPATH,'//button[contains(@class, "Button_Button__ra12g") and text()="Да"]') # Кнопка Да в всплывающем окне Хотите оформить заказ?
    ORDER_SUCCESS_ORDER_POPUP_HEADER = (By.XPATH, '//*[contains(@class, "Order_ModalHeader") and contains(text(), "Заказ оформлен")]') # Высплывающее окно Заказ оформлен
    
    # Локатор для станций метро в выпадающем списке
    @staticmethod
    def get_metro_option_locator(metro_station: str):
        return (By.XPATH, f'//div[@class="Order_Text__2broi" and text()="{metro_station}"]')
    
    # Локатор значения станции метро в плейсхолдере 
    @staticmethod
    def get_metro_placeholder_locator(metro_station: str):
        return (By.XPATH, f'//input[@placeholder="* Станция метро" and @value="{metro_station}"]')
    
    # Локатор для дат в выпадающем календаре
    @staticmethod
    def get_calendar_day_locator(day):
        return (By.XPATH, f'//div[contains(@aria-label, "{day}")]')
    
    # Локатор для выбора срока аренды
    @staticmethod
    def get_rental_term_option_locator(term_order: str):
        return (By.XPATH, f'//div[contains(@class, "Dropdown-option") and text()="{term_order}"]')

    # Локатор для выбора цвета самоката из чекбокса
    @staticmethod
    def get_colour_checkbox_locator(colour: str):
        for key, val in colours.items():
            if val == colour:
                return (By.ID, key)
