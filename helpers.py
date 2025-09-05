from locators.main_page_locators import MainPageLocator
from data import AnswerTexts

# Генерирует тестовые данные для проверки аккордеона в разделе 'Вопросы о важном' на главной странице.
def get_test_data_faq_accordion():
    test_data = []

    for index in AnswerTexts.answer_text:
        question_locator = MainPageLocator.get_question_locator(index)
        answer_locator = MainPageLocator.get_answer_locator(index)
        question_text = AnswerTexts.answer_text[index]["question"]
        expected_answer = AnswerTexts.answer_text[index]["answer"]

        test_case = (question_locator, answer_locator, question_text, expected_answer)
        test_data.append(test_case)

    return test_data

# Выделяет день и месяц для работы с выпадающим календарем на странице заказа
def extract_day_and_month_from_date(date_order):
    month_map = {'01': 'январь', '02': 'февраль', '03': 'март', '04': 'апрель', '05': 'май', '06': 'июнь', '07': 'июль',
                 '08': 'август', '09': 'сентябрь', '10': 'октябрь', '11': 'ноябрь', '12': 'декабрь'}
    date = date_order.split(".")
    month_number = date[1]
    month = month_map[month_number]
    day = f"{int(date[0])}-е"
    return day, month