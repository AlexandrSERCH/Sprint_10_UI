import allure
from selenium.common.exceptions import NoSuchElementException

from data.taxi.taxi_data import TaxiData
from locators.call_taxi_page_locators import CallTaxiPageLocators as L
from pages.base_page import BasePage


class CallTaxiPage(BasePage):

    @allure.step("Нажать кнопку 'Вызвать такси'")
    def confirm_order_taxi(self) -> None:
        self._click(L.CALL_TAXI)

    @allure.step("Проверить отображение 6 тарифов по ТЗ")
    def is_get_6_taxi_titles(self) -> bool:
        elements = self._find_elements(L.ELEMENTS_TAXI_TITLE)
        actual_titles = {el.text.strip() for el in elements if el.text.strip()}
        expected_titles = set(TaxiData.tariffs.TITLES)
        return actual_titles == expected_titles and len(actual_titles) == len(expected_titles)

    @allure.step("Проверить что один из тарифов активен")
    def is_one_active_taxi_title(self) -> bool:
        elements = self._find_elements(L.ELEMENTS_TAXI_TITLE)
        active_block = self._find_element(L.ACTIVE_TAXI_TITLE)
        for el in elements:
            try:
                active_block.find_element(*L.active_taxi_by_title(el.text))
                return True
            except NoSuchElementException:
                continue
        return False

    @allure.step("Получить описание тарифа: {taxi_title}")
    def get_tariff_description(self, taxi_title: str) -> str:
        self._click(L.taxi_title_locator(taxi_title))
        taxi_info = self._find_element(L.TAXI_INFO)
        self._hover(taxi_info)
        name = self._get_text(L.TARIFF_NAME)
        self._hover(taxi_info)
        description = self._get_text(L.TARIFF_DESCRIPTION)
        return f"{name} - {description}"

    @allure.step("Проверить видимость поля: {field_name}")
    def is_visible_order_field(self, field_name: str) -> bool:
        locator = L.ORDER_FIELD_MAP[field_name]
        return self._check_visible(locator)

    @allure.step("Выбрать тариф Рабочий, включить чекбокс, нажать 'Ввести номер и заказать'")
    def open_waiting_window(self) -> None:
        self._click(L.WORKING)
        self._scroll_to(L.REQUIREMENTS)
        self._click(L.REQUIREMENTS)
        self._scroll_to(L.LAPTOP_TABLE_TOGGLE)
        self._click(L.LAPTOP_TABLE_TOGGLE)
        self._click(L.BUTTON_ENTER_NUMBER_AND_ORDER)

    @allure.step("Ожидать окончания таймера поиска машины")
    def wait_for_timer_to_expire(self) -> None:
        self._long_wait_invisible(L.TIMER)

    @allure.step("Проверить заголовок 'Поиск машины'")
    def is_visible_search_header(self) -> bool:
        return self._check_visible(L.HEADER_OF_MODAL)

    @allure.step("Проверить таймер обратного отсчёта")
    def is_visible_timer(self) -> bool:
        return self._check_visible(L.TIMER)

    @allure.step("Проверить кнопку 'Отменить' в окне поиска")
    def is_visible_cancel_button(self) -> bool:
        return self._check_visible(L.CANCEL)

    @allure.step("Проверить кнопку 'Детали' в окне поиска")
    def is_visible_details_button(self) -> bool:
        return self._check_visible(L.ORDER_DETAILS)

    @allure.step("Проверить заголовок 'n мин. и приедет'")
    def is_visible_arrival_header(self) -> bool:
        return self._check_visible(L.HEADER_OF_FINAL_MODAL)

    @allure.step("Проверить номер автомобиля")
    def is_visible_auto_number(self) -> bool:
        return self._check_visible(L.AUTO_NUMBER)

    @allure.step("Проверить картинку автомобиля")
    def is_visible_auto_image(self) -> bool:
        return self._check_visible(L.AUTO_IMG)

    @allure.step("Проверить фото водителя")
    def is_visible_driver_photo(self) -> bool:
        return self._check_visible(L.DRIVER_PHOTO)

    @allure.step("Проверить рейтинг водителя")
    def is_visible_driver_rating(self) -> bool:
        return self._check_visible(L.DRIVER_RATING)

    @allure.step("Проверить кнопку 'Отменить' в финальном окне")
    def is_visible_cancel_in_final(self) -> bool:
        return self._check_visible(L.CANCEL)

    @allure.step("Проверить кнопку 'Детали' в финальном окне")
    def is_visible_details_in_final(self) -> bool:
        return self._check_visible(L.ORDER_DETAILS)

    @allure.step("Проверить что имя водителя из допустимого списка")
    def is_driver_name_valid(self) -> bool:
        name = self._get_text(L.DRIVER_NAME)
        return name in TaxiData.drivers.NAMES

    @allure.step("Получить стоимость до оформления заказа")
    def get_price_before_order(self) -> str:
        text = self._get_text(L.PRICE_BEFORE_ORDER)
        return text.split()[2]

    @allure.step("Получить стоимость в блоке 'Детали' после оформления заказа")
    def get_price_after_order(self) -> str:
        self._click(L.ORDER_DETAILS)
        text_after = self._get_text(L.PRICE_AFTER_ORDER)
        return text_after.split()[2].split("₽")[0]

    @allure.step("Нажать 'Отменить' и проверить закрытие модального окна")
    def is_modal_closed_after_cancel(self) -> bool:
        self._click(L.CANCEL)
        return self._wait_invisible(L.MODAL_WAITING)
