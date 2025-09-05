from selenium.webdriver.common.by import By

# Локаторы элементов главной страницы
class MainPageLocator:

    MAIN_PAGE_WORK_AREA = (By.CLASS_NAME, 'Home_FourPart__1uthg') # Рабочая область главной страницы
    ORDER_BUTTON_MIDDLE = (By.XPATH, "//button[contains(@class, 'Button_Middle__1CSJM')]") # Кнопка заказать в середине страниицы

    # Локатор вопроса в разделе "Вопросы о важном" по индексу (0-7)
    @staticmethod
    def get_question_locator(index):
        return (By.ID, f'accordion__heading-{index}')

    # Локатор ответа в разделе "Вопросы о важном" по индексу (0-7)
    @staticmethod 
    def get_answer_locator(index):
        return (By.ID, f'accordion__panel-{index}')
