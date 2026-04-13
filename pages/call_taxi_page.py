import allure
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from data.taxi.taxi_data import TaxiData
from pages.base_page import BasePage


class CallTaxiPage(BasePage):

    ACTIVE_TAXI_TITLE = (By.XPATH, '//div[@class="tcard active"]')
    ELEMENTS_TAXI_TITLE = (By.XPATH, '//div[@class="tcard-title"]')
    TAXI_INFO = (By.XPATH, '//div[@class="tcard active"]/button')
    TARIFF_NAME = (By.CSS_SELECTOR, 'div.tcard.active div.i-title')
    TARIFF_DESCRIPTION = (By.CSS_SELECTOR, 'div.tcard.active div.i-dPrefix')
    CALL_TAXI = (By.XPATH, '//button[text()="Вызвать такси"]')

    PHONE = (By.XPATH, '//div[text()="Телефон"]')
    PAYMENT_METHOD = (By.XPATH, '//div[@class="pp-button filled"]')
    COMMENT = (By.XPATH, '//label[text()="Комментарий водителю..."]')
    REQUIREMENTS_FOR_ORDER = (By.XPATH, '//div[@class="reqs-header"]')
    BUTTON_CREATE_ORDER = (By.XPATH, '//button[@class="smart-button"]')

    _ORDER_FIELD_MAP = {
        "Телефон": PHONE,
        "Способ оплаты": PAYMENT_METHOD,
        "Комментарий водителю": COMMENT,
        "Требования к заказу": REQUIREMENTS_FOR_ORDER,
        "Заказ тарифа Такси": BUTTON_CREATE_ORDER,
    }

    WORKING = (By.XPATH, '//div[@class="tcard-title" and text()="Рабочий"]')
    RAIDER = (By.XPATH, '//div[@class="reqs"]')
    LAPTOP_TABLE_TOGGLE = (By.XPATH, '//span[@class="slider round"]')
    BUTTON_ENTER_NUMBER_AND_ORDER = (By.XPATH, '//span[text()="Ввести номер и заказать"]')

    MODAL_WAITING = (By.XPATH, '//div[@class="order-body"]')
    CANCEL = (By.XPATH, '//button/following-sibling::div[text()="Отменить"]')
    ORDER_DETAILS = (By.XPATH, '//div[text()="Детали"]/parent::div')
    TIMER = (By.XPATH, '//div[@class="order-header-time"]')
    HEADER_OF_MODAL = (By.XPATH, '//div[@class="order-header-title" and text()="Поиск машины"]')

    HEADER_OF_FINAL_MODAL = (By.XPATH, '//div[contains(@class,"order-header-content") and contains(normalize-space(.),"мин. и приедет")]')
    AUTO_NUMBER = (By.CSS_SELECTOR, 'div.number')
    AUTO_IMG = (By.XPATH, '//img[contains(translate(@alt,"CAR","car"),"car")]')
    DRIVER_NAME = (By.XPATH, '//div[@class="order-button"]/following-sibling::div')
    DRIVER_FOTO = (By.XPATH, '//div[contains(@class, "rating")]/following-sibling::img[@alt="close"]')
    DRIVER_RATING = (By.XPATH, '//div[@class="order-btn-rating"]')
    PRICE_AFTER_ORDER = (By.XPATH, '//div[text()="Еще про поездку"]/following-sibling::div')
    PRICE_BEFORE_ORDER = (By.XPATH, '//div[@class="text"]')

    @staticmethod
    def _active_taxi_by_title(taxi_title: str) -> tuple:
        return By.XPATH, f'//div[@class="tcard active"]/div[text()="{taxi_title}"]'

    @staticmethod
    def _taxi_title_locator(taxi_title: str) -> tuple:
        return By.XPATH, f'//div[@class="tcard-title" and text()="{taxi_title}"]'

    @allure.step("Нажать кнопку 'Вызвать такси'")
    def confirm_order_taxi(self) -> None:
        self._click(self.CALL_TAXI)

    @allure.step("Проверить отображение 6 тарифов по ТЗ")
    def is_get_6_taxi_titles(self) -> bool:
        elements = self._find_elements(self.ELEMENTS_TAXI_TITLE)
        actual_titles = {el.text.strip() for el in elements if el.text.strip()}
        expected_titles = set(TaxiData.tariffs.TITLES)
        return actual_titles == expected_titles and len(actual_titles) == len(expected_titles)

    @allure.step("Проверить что один из тарифов активен")
    def is_one_active_taxi_title(self) -> bool:
        elements = self._find_elements(self.ELEMENTS_TAXI_TITLE)
        active_block = self._find_element(self.ACTIVE_TAXI_TITLE)
        for el in elements:
            try:
                active_block.find_element(*self._active_taxi_by_title(el.text))
                return True
            except NoSuchElementException:
                continue
        return False

    @allure.step("Получить описание тарифа: {taxi_title}")
    def get_tariff_description(self, taxi_title: str) -> str:
        self._click(self._taxi_title_locator(taxi_title))
        taxi_info = self._find_element(self.TAXI_INFO)
        self._hover(taxi_info)
        name = self._get_text(self.TARIFF_NAME)
        self._hover(taxi_info)
        description = self._get_text(self.TARIFF_DESCRIPTION)
        return f"{name} - {description}"

    @allure.step("Проверить видимость поля: {field_name}")
    def is_visible_order_field(self, field_name: str) -> bool:
        locator = self._ORDER_FIELD_MAP[field_name]
        return self._check_visible(locator)

    @allure.step("Выбрать тариф Рабочий, включить чекбокс, нажать 'Ввести номер и заказать'")
    def open_waiting_window(self) -> None:
        self._click(self.WORKING)
        self._scroll_to(self.RAIDER)
        self._click(self.RAIDER)
        self._scroll_to(self.LAPTOP_TABLE_TOGGLE)
        self._click(self.LAPTOP_TABLE_TOGGLE)
        self._click(self.BUTTON_ENTER_NUMBER_AND_ORDER)

    @allure.step("Ожидать окончания таймера поиска машины")
    def wait_for_timer_to_expire(self) -> None:
        self._long_wait_invisible(self.TIMER)

    @allure.step("Проверить заголовок 'Поиск машины'")
    def is_visible_search_header(self) -> bool:
        return self._check_visible(self.HEADER_OF_MODAL)

    @allure.step("Проверить таймер обратного отсчёта")
    def is_visible_timer(self) -> bool:
        return self._check_visible(self.TIMER)

    @allure.step("Проверить кнопку 'Отменить' в окне поиска")
    def is_visible_cancel_button(self) -> bool:
        return self._check_visible(self.CANCEL)

    @allure.step("Проверить кнопку 'Детали' в окне поиска")
    def is_visible_details_button(self) -> bool:
        return self._check_visible(self.ORDER_DETAILS)

    @allure.step("Проверить заголовок 'n мин. и приедет'")
    def is_visible_arrival_header(self) -> bool:
        return self._check_visible(self.HEADER_OF_FINAL_MODAL)

    @allure.step("Проверить номер автомобиля")
    def is_visible_auto_number(self) -> bool:
        return self._check_visible(self.AUTO_NUMBER)

    @allure.step("Проверить картинку автомобиля")
    def is_visible_auto_image(self) -> bool:
        return self._check_visible(self.AUTO_IMG)

    @allure.step("Проверить фото водителя")
    def is_visible_driver_photo(self) -> bool:
        return self._check_visible(self.DRIVER_FOTO)

    @allure.step("Проверить рейтинг водителя")
    def is_visible_driver_rating(self) -> bool:
        return self._check_visible(self.DRIVER_RATING)

    @allure.step("Проверить кнопку 'Отменить' в финальном окне")
    def is_visible_cancel_in_final(self) -> bool:
        return self._check_visible(self.CANCEL)

    @allure.step("Проверить кнопку 'Детали' в финальном окне")
    def is_visible_details_in_final(self) -> bool:
        return self._check_visible(self.ORDER_DETAILS)

    @allure.step("Проверить что имя водителя из допустимого списка")
    def is_driver_name_valid(self) -> bool:
        name = self._get_text(self.DRIVER_NAME)
        return name in TaxiData.drivers.NAMES

    @allure.step("Проверить совпадение цены до и после оформления заказа")
    def is_price_equal_before_and_after(self) -> bool:
        text = self._get_text(self.PRICE_BEFORE_ORDER)
        price_before = text.split()[2]
        self.confirm_order_taxi()
        self.open_waiting_window()
        self._click(self.ORDER_DETAILS)
        text_after = self._get_text(self.PRICE_AFTER_ORDER)
        price_after = text_after.split()[2].split("₽")[0]
        return price_before == price_after

    @allure.step("Нажать 'Отменить' и проверить закрытие модального окна")
    def is_modal_closed_after_cancel(self) -> bool:
        self._click(self.CANCEL)
        return self._wait_invisible(self.MODAL_WAITING)
