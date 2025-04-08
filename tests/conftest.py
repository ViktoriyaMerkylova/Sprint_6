import pytest
from selenium import webdriver
from curl import Curl


@pytest.fixture
def driver():
    browser = webdriver.Firefox()
    browser.get(Curl.URL_SAMOKAT)

    yield browser
    browser.quit()

