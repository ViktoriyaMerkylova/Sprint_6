import allure
from locators.important_questions_locators import ImportalQuestionLocators
from pages.order_verification_pages import OrderVerificationPages
from pages.important_questions_page import ImportantQuestionsPage
from pages.dzen_page import DzenPage


@allure.feature('Переходы на страницу "Яндекс Самокат", "Дзен" по кликам на лого')
class TestClickToLogo:
    @allure.title('Тест перехода на страницу "Яндекс Самокат"')
    @allure.description('Клик на лого "Самокат"  > переход на главную страницу "Яндекс Самокат"')
    def test_go_to_scooter_home_page_by_clicking_on_scooter_logo(self, driver):
        main_page = ImportantQuestionsPage(driver)
        main_page.click_order_button(ImportalQuestionLocators.header_order_button)
        order_page = OrderVerificationPages(driver)
        order_page.click_scooter_logo()
        main_page.check_go_to_home_page()

    @allure.title('Тест перехода на страницу "Dzen"')
    @allure.description('Клик по лого "Яндекс" > переход на страницу "Dzen"')
    def test_go_to_dzen_click_yandex_logo(self, driver):
        main_page = ImportantQuestionsPage(driver)
        main_page.click_yandex_logo()
        main_page.go_to_dzen()
        dzen_page = DzenPage(driver)
        dzen_page.loading_dzen_page()
        dzen_page.check_go_to_dzen()