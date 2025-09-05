import allure
from pages.base_page import BasePage


# FAQ с выпадающим списком раздела "Вопросы о важном"
class MainPageFAQ(BasePage):

    @allure.step('Кликаем на вопрос: "{question_text}"')
    def click_accordion(self, question_locator, question_text):
        self.scroll_to_element(question_locator)
        self.click_on_element(question_locator)

    @allure.step('Ждем появления ответа')
    def wait_for_answer_visible(self, answer_locator):
        self.wait_for_element(answer_locator)

    @allure.step('Получаем текст из раскрытого ответа')
    def get_answer_text(self, answer_locator):
        return self.get_text_element(answer_locator)

    @allure.step("Сравниваем текст ответа c ожидаемым")
    def check_answer_text(self, answer_locator, expected_answer):
        actual_text = self.get_answer_text(answer_locator)
        return actual_text == expected_answer


# Кнопки заказать    
class MainPageOrderButton(BasePage):   

    @allure.step("Кликаем на кнопку Заказать")
    def click_order_button(self, order_button):
        self.scroll_to_element(order_button)
        self.click_on_element(order_button)
