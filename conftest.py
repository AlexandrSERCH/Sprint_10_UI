import os

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import constants
from data.taxi.taxi_data import TaxiData
from pages.call_taxi_page import CallTaxiPage
from pages.main_page import MainPage
from utils.attach import attach_screenshot


@pytest.fixture(autouse=True)
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    attach_screenshot(driver)
    driver.quit()


@pytest.fixture
def main_page(browser) -> MainPage:
    page = MainPage(browser)
    page.open()
    return page


@pytest.fixture
def call_taxi_page(main_page) -> CallTaxiPage:
    main_page.add_two_address(TaxiData.addresses.LOCATION_1, TaxiData.addresses.LOCATION_2)
    main_page.confirm_order_taxi()
    return CallTaxiPage(main_page.driver)


@pytest.fixture
def call_taxi_page_waiting(call_taxi_page) -> CallTaxiPage:
    call_taxi_page.open_waiting_window()
    return call_taxi_page


@pytest.fixture
def call_taxi_page_final(call_taxi_page_waiting) -> CallTaxiPage:
    call_taxi_page_waiting.wait_for_timer_to_expire()
    return call_taxi_page_waiting


@pytest.fixture
def call_taxi_page_price(main_page) -> CallTaxiPage:
    main_page.add_two_address(TaxiData.addresses.LOCATION_1, TaxiData.addresses.LOCATION_2)
    return CallTaxiPage(main_page.driver)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Хук для снятия скриншота в момент падения теста.
    Срабатывает при наличии поп-апов, невидимых элементов и других UI-аномалий.
    """
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("browser")
        if driver:
            with allure.step("Скриншот при падении"):
                attach_screenshot(driver)
