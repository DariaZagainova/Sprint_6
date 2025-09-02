import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидаем видимость элемента')
    def wait_for_element(self, locator, timeout = 10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step('Скролл до элемента')
    def scroll_to_element(self, locator, timeout = 10):
        element = self.wait_for_element(locator,timeout)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step('Клик на элемент')
    def click_on_element(self, locator, timeout = 10):
        element = self.wait_for_element(locator,timeout)
        element.click()

    @allure.step('Вводим текст в поле ввода')
    def send_keys_to_input(self, locator, keys, timeout = 10):
        element = self.wait_for_element(locator,timeout)
        element.clear()
        element.send_keys(keys)

    @allure.step('Получаем текст элемента')
    def get_text_element(self, locator, timeout = 10):
        element = self.wait_for_element(locator,timeout)
        return element.text
    
    @allure.step("Получить значение поля ввода")
    def get_value_element(self, locator, timeout = 10):
        element = self.wait_for_element(locator, timeout)
        return element.get_attribute("value")
    
    @allure.step('Получаем URL текущей страницы')
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step('Получаем список текущих открытых вкладок (окон) браузера.')
    def get_open_windows(self):
        open_windows = self.driver.window_handles
        return open_windows

    @allure.step('Ожидание открытия нового окна или вкладки в браузере')
    def wait_for_new_window_opened(self, open_windows, timeout = 10):
        WebDriverWait(self.driver, timeout).until(lambda d: len(d.window_handles) > len(open_windows))

    @allure.step('Получаем идентификатор нового окна')
    def get_new_window_handle(self, open_windows):
        new_windows = self.driver.window_handles
        new_window = [w for w in new_windows if w not in open_windows]
        return new_window[0]

    @allure.step('Переключаемся на новое окно')
    def switch_to_window(self, new_window):
        self.driver.switch_to.window(new_window)

    @allure.step('Ожидаем, пока URL изменится')
    def wait_for_url_to_change_from_blank(self, expected_url, timeout = 10):
        WebDriverWait(self.driver, timeout).until(lambda d: d.current_url == expected_url)

    @allure.step('Переход на новое окно')
    def switch_to_new_window(self, open_windows, expected_url):
        self.wait_for_new_window_opened(open_windows)    
        new_window = self.get_new_window_handle(open_windows)
        self.switch_to_window(new_window)
        self.wait_for_url_to_change_from_blank(expected_url)
   
    @allure.step('Проверяем, что элемент выбран')
    def is_element_selected(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        return element.is_selected()
    