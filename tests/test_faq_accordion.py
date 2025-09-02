import pytest
import allure
from pages.main_page import MainPageFAQ
from helpers import get_test_data_faq_accordion
 
@allure.sub_suite ('class TestFaqAccordion: Раздел "Вопросы о важном". Проверки, что при нажатии на вопрос открывается соответствующий ответ.')
class TestFaqAccordion:

    @allure.title('На вопрос "{question_text}" - ответ "{expected_answer}"')
    @pytest.mark.parametrize('question_locator, answer_locator, question_text, expected_answer', get_test_data_faq_accordion())
    def test_click_accordion_shows_correct_answer(self, driver, question_locator, answer_locator, question_text, expected_answer):
        main_page = MainPageFAQ(driver)
        main_page.click_accordion(question_locator, question_text)
        main_page.wait_for_answer_visible(answer_locator)

        assert main_page.check_answer_text(answer_locator, expected_answer), f'Ответ не совпадает! Ожидалось: "{expected_answer}" Фактически: "{main_page.get_answer_text(answer_locator)}"'
