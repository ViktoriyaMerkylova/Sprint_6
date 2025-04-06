import allure
from selenium.webdriver.common.by import By
from pages.base_pages import BasePages


class DzenPage(BasePages):
    dzen_logo_in_header = (By.CSS_SELECTOR, ".dzen-layout--desktop-base-header__logo-2H")

    @allure.step('Ожидание загрузки главной страницы "Дзен"')
    def loading_dzen_page(self):
        self.wait_for_visibility_of_element(self.dzen_logo_in_header)

    @allure.step('Проверка открытия страницы "Дзен"')
    def check_go_to_dzen(self):
        current_url = self.get_current_url()
        assert current_url == "https://dzen.ru/?yredirect=true", 'Главная страница "Дзен" не открылась'

