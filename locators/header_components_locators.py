from selenium.webdriver.common.by import By

# Локаторы элементов из шапки страниц
class HeaderComponentsLocator:

    SCOOTER_LOGO = (By.CSS_SELECTOR, 'a.Header_LogoScooter__3lsAR[href="/"]') # Логотип Самокат
    YANDEX_LOGO = (By.CLASS_NAME, 'Header_LogoYandex__3TSOI') # Логотип Яндекс
    ORDER_BUTTON_HEADER = (By.XPATH, "//div[@class='Header_Nav__AGCXC']/button[text()='Заказать']") # Кнопка Заказать
