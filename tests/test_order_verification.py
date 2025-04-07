import pytest
import allure
from locators.order_verification_locators import OrderVerificationLocators
from locators.important_questions_locators import ImportalQuestionLocators
from data import Data
from pages.order_verification_pages import OrderVerificationPages
from pages.important_questions_page import ImportantQuestionsPage

@allure.feature('Заказ самоката')
class TestOrderVerification:

    @allure.title('Тест заказа доставки самоката')
    @allure.description(
        'Кликнуть на кнопку "Заказать", заполнить форму валидными данными, появляется окно "Посмотреть статус" '
    )
    @pytest.mark.parametrize(
        'order_button, customer_data, metro_button, rental_data, days_button, colour_button',
        [
            [ImportalQuestionLocators.header_order_button, Data.user_one, OrderVerificationLocators.metro_zorge_st,
             Data.terms_one, OrderVerificationLocators.one_day_period, OrderVerificationLocators.scooter_colour_black],
            [ImportalQuestionLocators.center_order_button, Data.user_two, OrderVerificationLocators.metro_lubjanka_st,
             Data.terms_two, OrderVerificationLocators.four_day_period, OrderVerificationLocators.scooter_colour_gray]
        ]
    )
    def test_scooter_orders(self, driver, order_button, customer_data, metro_button, rental_data,
                            days_button, colour_button):
        main_page = ImportantQuestionsPage(driver)
        main_page.click_order_button(order_button)
        order_page = OrderVerificationPages(driver)
        order_page.fill_out_customer_form(*customer_data, metro_button)
        order_page.click_next_button()
        order_page.fill_out_rental_form(*rental_data, days_button, colour_button)
        order_page.click_order_button()
        order_page.wait_for_load_order_header()
        order_page.click_yes_button()
        order_page.check_success_window()
