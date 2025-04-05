import pytest
from selenium import webdriver
from curl import main_site


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(main_site)
    yield driver
    driver.quit()