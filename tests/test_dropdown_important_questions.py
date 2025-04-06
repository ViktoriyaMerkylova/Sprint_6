import pytest
import allure
from Locators.important_questions_locators import ImportalQuestionLocators
from data import Data
from pages.important_questions_page import ImportantQuestionsPage


@allure.feature('FAQ на главной странице "Яндекс Самокат"')
class TestHomePage:
    @allure.title('Тест открытия ответов в FAQ')
    @allure.description('Клик по вопросам FAQ по очереди, открываются ответы на вопросы по очереди')
    @pytest.mark.parametrize(
        'button, answer, expected_text',
        [
            [ImportalQuestionLocators.first_question_button, ImportalQuestionLocators.first_answer_text,
             Data.coast_ans],
            [ImportalQuestionLocators.second_question_button, ImportalQuestionLocators.second_answer_text,
             Data.share_ans],
            [ImportalQuestionLocators.third_rent_question_button, ImportalQuestionLocators.third_rent_answer_text,
             Data.time_rent_ans],
            [ImportalQuestionLocators.fourth_rent_question_button, ImportalQuestionLocators.fourth_rent_answer_text,
             Data.today_rent_ans],
            [ImportalQuestionLocators.fifth_return_question_button, ImportalQuestionLocators.fifth_return_answer_text,
             Data.extend_return_ans],
            [ImportalQuestionLocators.sixth_question_button, ImportalQuestionLocators.sixth_answer_text,
             Data.charge_ans],
            [ImportalQuestionLocators.seventh_order_question_button, ImportalQuestionLocators.seventh_order_answer_text,
             Data.cancel_order_ans],
            [ImportalQuestionLocators.eighth_question_button, ImportalQuestionLocators.eighth_answer_text,
             Data.mkad_ans]
        ]
    )
    def test_faq_list_click_on_questions_check_answer(self, driver, button, answer, expected_text):
        main_page = ImportantQuestionsPage(driver)
        main_page.click_question_button(button)
        main_page.check_answer_text(answer, expected_text)

