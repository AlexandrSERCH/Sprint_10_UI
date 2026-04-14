import allure

from data.taxi.taxi_data import TaxiData
from utils.markers import tag, severity, Level


@allure.epic("Маршруты")
@allure.feature("Отображение маршрута на карте")
class TestRouteDrawing:

    @severity(Level.NORMAL)
    @tag("UI", "smoke", "regress", "routes")
    @allure.title("При вводе двух разных адресов на карте отображаются две точки маршрута")
    def test_two_route_dots_visible_on_map(self, main_page):
        main_page.add_two_address(TaxiData.addresses.LOCATION_1, TaxiData.addresses.LOCATION_2)
        assert main_page.drawing_a_route()
