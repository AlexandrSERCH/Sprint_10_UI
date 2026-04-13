import allure

import constants
from locators.main_page_locators import MainPageLocators as L
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Открыть главную страницу")
    def open(self) -> None:
        self._open_page(constants.MAIN_PAGE_URL)

    @allure.step("Ввести адрес отправления: '{from_address}' и назначения: '{to_address}'")
    def add_two_address(self, from_address: str, to_address: str) -> None:
        self._send_keys(L.FROM_FIELD, from_address)
        self._send_keys(L.TO_FIELD, to_address)

    @allure.step("Нажать кнопку 'Вызвать такси'")
    def confirm_order_taxi(self) -> None:
        self._click(L.CALL_TAXI)

    @allure.step("Проверить отображение двух точек маршрута на карте")
    def drawing_a_route(self) -> tuple[bool, bool]:
        return (
            self._check_visible(L.FROM_DOT),
            self._check_visible(L.TO_DOT),
        )

    @allure.step("Проверить видимость блока выбора маршрута")
    def is_route_block_visible(self) -> bool:
        for locator in L.LOCATORS_OF_CHOICE:
            if not self._check_visible(locator):
                return False
        return True

    @allure.step("Получить текст блока маршрута")
    def get_route_info_text(self) -> list:
        return self._get_texts(L.TYPE_AND_PRICE_DELIVERY, L.TRAVEL_TIME)

    @allure.step("Проверить изменение данных маршрута при переключении Быстрый → Оптимальный")
    def is_route_data_changed_on_tab_switch(self) -> bool:
        text_quick = self._get_texts(L.TYPE_AND_PRICE_DELIVERY, L.TRAVEL_TIME)
        self._click(L.OPTIMA)
        text_optima = self._get_texts(L.TYPE_AND_PRICE_DELIVERY, L.TRAVEL_TIME)
        return text_quick != text_optima

    @allure.step("Получить текст активного таба после переключения на Оптимальный")
    def get_active_tab_text(self) -> str:
        self._click(L.OPTIMA)
        return self._get_text(L.ACTIVE_TAB)

    @allure.step("Проверить кликабельность всех типов транспорта в маршруте Свой")
    def is_all_transport_clickable_in_own(self) -> bool:
        self._click(L.OWN)
        for locator in L.LOCATORS_OF_TRANSPORT:
            if not self._is_clickable(locator):
                return False
        return True

    @allure.step("Проверить активность кнопки 'Вызвать такси'")
    def is_call_taxi_button_active(self) -> bool:
        return self._is_clickable(L.CALL_TAXI)

    @allure.step("Проверить активность кнопки 'Забронировать' для маршрута Свой, тип Драйв")
    def is_confirmation_button_active(self) -> bool:
        self._click(L.OWN)
        self._is_visible(L.TYPE_DRIVE)
        self._click(L.TYPE_DRIVE)
        self._is_visible(L.CONFIRMATION)
        return self._is_clickable(L.CONFIRMATION)
