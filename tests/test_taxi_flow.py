import allure
import pytest

from utils.markers import tag, severity, Level


@allure.epic("Такси")
@allure.feature("Поиск и назначение водителя")
class TestTaxiFlow:

    @severity(Level.CRITICAL)
    @tag("UI", "smoke", "regress", "taxi")
    @allure.title("В окне 'Поиск машины' отображается заголовок")
    def test_waiting_window_has_search_header(self, call_taxi_page_waiting):
        call_taxi_page_waiting.open_waiting_window()
        assert call_taxi_page_waiting.is_visible_search_header(), (
            "Заголовок 'Поиск машины' не отображается"
        )

    @severity(Level.NORMAL)
    @tag("UI", "regress", "taxi")
    @allure.title("В окне 'Поиск машины' отображается таймер обратного отсчёта")
    def test_waiting_window_has_timer(self, call_taxi_page_waiting):
        call_taxi_page_waiting.open_waiting_window()
        assert call_taxi_page_waiting.is_visible_timer(), (
            "Таймер обратного отсчёта не отображается"
        )

    @severity(Level.NORMAL)
    @tag("UI", "regress", "taxi")
    @allure.title("В окне 'Поиск машины' отображается кнопка 'Отменить'")
    def test_waiting_window_has_cancel_button(self, call_taxi_page_waiting):
        call_taxi_page_waiting.open_waiting_window()
        assert call_taxi_page_waiting.is_visible_cancel_button(), (
            "Кнопка 'Отменить' не отображается в окне поиска"
        )

    @severity(Level.NORMAL)
    @tag("UI", "regress", "taxi")
    @allure.title("В окне 'Поиск машины' отображается кнопка 'Детали'")
    def test_waiting_window_has_details_button(self, call_taxi_page_waiting):
        call_taxi_page_waiting.open_waiting_window()
        assert call_taxi_page_waiting.is_visible_details_button(), (
            "Кнопка 'Детали' не отображается в окне поиска"
        )

    @severity(Level.CRITICAL)
    @tag("UI", "regress", "taxi")
    @allure.title("В финальном окне отображается заголовок 'n мин. и приедет'")
    def test_final_window_has_arrival_header(self, call_taxi_page_final):
        call_taxi_page_final.wait_for_timer_to_expire()
        assert call_taxi_page_final.is_visible_arrival_header(), (
            "Заголовок 'n мин. и приедет' не отображается"
        )

    @severity(Level.NORMAL)
    @tag("UI", "regress", "taxi")
    @allure.title("В финальном окне отображается номер автомобиля")
    def test_final_window_has_auto_number(self, call_taxi_page_final):
        call_taxi_page_final.wait_for_timer_to_expire()
        assert call_taxi_page_final.is_visible_auto_number(), (
            "Номер автомобиля не отображается"
        )

    @severity(Level.NORMAL)
    @tag("UI", "regress", "taxi")
    @allure.title("В финальном окне отображается картинка автомобиля")
    def test_final_window_has_auto_image(self, call_taxi_page_final):
        call_taxi_page_final.wait_for_timer_to_expire()
        assert call_taxi_page_final.is_visible_auto_image(), (
            "Картинка автомобиля не отображается"
        )

    @severity(Level.NORMAL)
    @tag("UI", "regress", "taxi")
    @allure.title("В финальном окне отображается фото водителя")
    def test_final_window_has_driver_photo(self, call_taxi_page_final):
        call_taxi_page_final.wait_for_timer_to_expire()
        assert call_taxi_page_final.is_visible_driver_photo(), (
            "Фото водителя не отображается"
        )

    @severity(Level.NORMAL)
    @tag("UI", "regress", "taxi")
    @allure.title("В финальном окне отображается рейтинг водителя")
    def test_final_window_has_driver_rating(self, call_taxi_page_final):
        call_taxi_page_final.wait_for_timer_to_expire()
        assert call_taxi_page_final.is_visible_driver_rating(), (
            "Рейтинг водителя не отображается"
        )

    @severity(Level.NORMAL)
    @tag("UI", "regress", "taxi")
    @allure.title("В финальном окне отображается кнопка 'Отменить'")
    def test_final_window_has_cancel_button(self, call_taxi_page_final):
        call_taxi_page_final.wait_for_timer_to_expire()
        assert call_taxi_page_final.is_visible_cancel_in_final(), (
            "Кнопка 'Отменить' не отображается в финальном окне"
        )

    @severity(Level.NORMAL)
    @tag("UI", "regress", "taxi")
    @allure.title("В финальном окне отображается кнопка 'Детали'")
    def test_final_window_has_details_button(self, call_taxi_page_final):
        call_taxi_page_final.wait_for_timer_to_expire()
        assert call_taxi_page_final.is_visible_details_in_final(), (
            "Кнопка 'Детали' не отображается в финальном окне"
        )

    @severity(Level.NORMAL)
    @tag("UI", "regress", "taxi")
    @allure.title("Имя водителя присутствует в списке допустимых имён")
    def test_driver_name_is_valid(self, call_taxi_page_final):
        call_taxi_page_final.wait_for_timer_to_expire()
        assert call_taxi_page_final.is_driver_name_valid(), (
            "Имя водителя не из допустимого списка"
        )

    @severity(Level.NORMAL)
    @tag("UI", "regress", "taxi")
    @allure.title("Стоимость в блоке 'Детали' совпадает со стоимостью до заказа")
    def test_price_matches_before_and_after_order(self, call_taxi_page):
        price_before = call_taxi_page.get_price_before_order()
        call_taxi_page.confirm_order_taxi()
        call_taxi_page.open_waiting_window()
        price_after = call_taxi_page.get_price_after_order()
        assert price_before == price_after, (
            f"Цена до заказа: '{price_before}', в блоке 'Детали': '{price_after}'"
        )

    @pytest.mark.xfail(reason="Баг: кнопка 'Отменить' не кликабельна")
    @severity(Level.NORMAL)
    @tag("UI", "regress", "taxi")
    @allure.title("Нажатие кнопки 'Отменить' закрывает модальное окно")
    def test_cancel_button_closes_modal(self, call_taxi_page_waiting):
        call_taxi_page_waiting.open_waiting_window()
        assert call_taxi_page_waiting.is_modal_closed_after_cancel()
