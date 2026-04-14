import allure
import pytest
from selenium import webdriver

from data.taxi.taxi_data import TaxiData
from pages.call_taxi_page import CallTaxiPage
from pages.main_page import MainPage
from utils.attach import attach_screenshot


@pytest.fixture(autouse=True)
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.fixture
def main_page(browser) -> MainPage:
    page = MainPage(browser)
    page.open()
    return page


@pytest.fixture
def main_page_with_route(main_page) -> MainPage:
    main_page.add_two_address(TaxiData.addresses.LOCATION_1, TaxiData.addresses.LOCATION_2)
    return main_page


@pytest.fixture
def call_taxi_page(main_page_with_route) -> CallTaxiPage:
    return CallTaxiPage(main_page_with_route.driver)


@pytest.fixture
def call_taxi_page_waiting(call_taxi_page) -> CallTaxiPage:
    call_taxi_page.confirm_order_taxi()
    return call_taxi_page


@pytest.fixture
def call_taxi_page_final(call_taxi_page_waiting) -> CallTaxiPage:
    call_taxi_page_waiting.open_waiting_window()
    return call_taxi_page_waiting


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("browser")
        if driver:
            with allure.step("Скриншот при падении"):
                attach_screenshot(driver)
