import allure
from selenium.webdriver.common.by import By

import constants
from data.taxi.taxi_data import TaxiData
from pages.base_page import BasePage


class MainPage(BasePage):

    FROM_FIELD = (By.XPATH, '//input[@id="from"]')
    TO_FIELD = (By.XPATH, '//input[@id="to"]')
    FROM_DOT = (By.XPATH, '//ymaps[contains(@class,"ff3333")]')
    TO_DOT = (By.XPATH, '//ymaps[contains(@class,"4296ea")]')

    OPTIMA = (By.XPATH, '//div[text()="Оптимальный"]')
    QUICK = (By.XPATH, '//div[text()="Быстрый"]')
    TYPE_AND_PRICE_DELIVERY = (By.XPATH, '//div[@class="text"]')
    TRAVEL_TIME = (By.XPATH, '//div[@class="duration"]')
    CALL_TAXI = (By.XPATH, '//button[text()="Вызвать такси"]')

    LOCATORS_OF_CHOICE = (OPTIMA, QUICK, TYPE_AND_PRICE_DELIVERY, TRAVEL_TIME, CALL_TAXI)

    OWN = (By.XPATH, '//div[text()="Свой"]')
    ACTIVE_TAB = (By.XPATH, '//div[@class="mode active"]')
    TYPE_CAR = (By.XPATH, '//div/img[contains(@src,"car.")]')
    TYPE_WALK = (By.XPATH, '//img[contains(@src,"walk")]')
    TYPE_TAXI = (By.XPATH, '//img[contains(@src,"taxi")]')
    TYPE_BIKE = (By.XPATH, '//img[contains(@src,"bike")]')
    TYPE_SCOOTER = (By.XPATH, '//img[contains(@src,"scooter")]')
    TYPE_DRIVE = (By.XPATH, '//img[contains(@src,"drive")]')
    LOCATORS_OF_TRANSPORT = (TYPE_WALK, TYPE_TAXI, TYPE_BIKE, TYPE_SCOOTER, TYPE_DRIVE, TYPE_CAR)

    CONFIRMATION = (By.XPATH, '//button[text()="Забронировать"]')

    @allure.step("Открыть главную страницу")
    def open(self) -> None:
        self._open_page(constants.main_page_url())

    @allure.step("Ввести адрес отправления: '{from_address}' и назначения: '{to_address}'")
    def add_two_address(self, from_address: str, to_address: str) -> None:
        self._send_keys(self.FROM_FIELD, from_address)
        self._send_keys(self.TO_FIELD, to_address)

    @allure.step("Нажать кнопку 'Вызвать такси'")
    def confirm_order_taxi(self) -> None:
        self._click(self.CALL_TAXI)

    @allure.step("Проверить отображение двух точек маршрута на карте")
    def drawing_a_route(self) -> tuple[bool, bool]:
        return (
            self._check_visible(self.FROM_DOT),
            self._check_visible(self.TO_DOT),
        )

    @allure.step("Проверить видимость блока выбора маршрута")
    def is_route_block_visible(self) -> bool:
        for locator in self.LOCATORS_OF_CHOICE:
            if not self._check_visible(locator):
                return False
        return True

    @allure.step("Ввести одинаковый адрес и получить текст блока маршрута")
    def get_same_address_route_text(self) -> list:
        self.add_two_address(TaxiData.addresses.LOCATION_1, TaxiData.addresses.LOCATION_1)
        return self._get_texts(self.TYPE_AND_PRICE_DELIVERY, self.TRAVEL_TIME)

    @allure.step("Проверить изменение данных маршрута при переключении Быстрый → Оптимальный")
    def is_route_data_changed_on_tab_switch(self) -> bool:
        text_quick = self._get_texts(self.TYPE_AND_PRICE_DELIVERY, self.TRAVEL_TIME)
        self._click(self.OPTIMA)
        text_optima = self._get_texts(self.TYPE_AND_PRICE_DELIVERY, self.TRAVEL_TIME)
        return text_quick != text_optima

    @allure.step("Получить текст активного таба после переключения на Оптимальный")
    def get_active_tab_text(self) -> str:
        self._click(self.OPTIMA)
        return self._get_text(self.ACTIVE_TAB)

    @allure.step("Проверить кликабельность всех типов транспорта в маршруте Свой")
    def is_all_transport_clickable_in_own(self) -> bool:
        self._click(self.OWN)
        for locator in self.LOCATORS_OF_TRANSPORT:
            if not self._is_clickable(locator):
                return False
        return True

    @allure.step("Проверить активность кнопки 'Вызвать такси'")
    def is_call_taxi_button_active(self) -> bool:
        return self._is_clickable(self.CALL_TAXI)

    @allure.step("Проверить активность кнопки 'Забронировать' для маршрута Свой, тип Драйв")
    def is_confirmation_button_active(self) -> bool:
        self._click(self.OWN)
        self._is_visible(self.TYPE_DRIVE)
        self._click(self.TYPE_DRIVE)
        self._is_visible(self.CONFIRMATION)
        return self._is_clickable(self.CONFIRMATION)
