import allure

from data.taxi.taxi_data import TaxiData
from utils.markers import tag, severity, Level


@allure.epic("Маршруты")
@allure.feature("Переключение вкладок маршрута")
class TestTaxiPreparation:

    @severity(Level.NORMAL)
    @tag("UI", "regress", "routes")
    @allure.title("При переключении Быстрый → Оптимальный пересчитываются время и стоимость")
    def test_route_data_changes_on_tab_switch(self, main_page_with_route):
        assert main_page_with_route.is_route_data_changed_on_tab_switch()

    @severity(Level.NORMAL)
    @tag("UI", "regress", "routes")
    @allure.title("После переключения на Оптимальный активен таб 'Оптимальный'")
    def test_active_tab_is_optima_after_switch(self, main_page_with_route):
        active_tab = main_page_with_route.get_active_tab_text()
        assert active_tab == TaxiData.route.ACTIVE_TAB, (
            f"Ожидался таб '{TaxiData.route.ACTIVE_TAB}', получен '{active_tab}'"
        )

    @severity(Level.NORMAL)
    @tag("UI", "regress", "routes")
    @allure.title("В маршруте Свой все виды транспорта становятся кликабельными")
    def test_all_transport_types_clickable_in_own(self, main_page_with_route):
        assert main_page_with_route.is_all_transport_clickable_in_own()

    @severity(Level.CRITICAL)
    @tag("UI", "smoke", "regress", "routes")
    @allure.title("В маршруте Быстрый активна кнопка 'Вызвать такси'")
    def test_call_taxi_button_is_active(self, main_page_with_route):
        assert main_page_with_route.is_call_taxi_button_active()

    @severity(Level.NORMAL)
    @tag("UI", "regress", "routes")
    @allure.title("В маршруте Свой, транспорт Драйв, активна кнопка 'Забронировать'")
    def test_confirmation_button_is_active_for_drive(self, main_page_with_route):
        assert main_page_with_route.is_confirmation_button_active()
