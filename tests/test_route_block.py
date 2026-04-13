import allure

from data.taxi.taxi_data import TaxiData
from utils.markers import tag, severity, Level


@allure.epic("Маршруты")
@allure.feature("Блок выбора маршрута")
class TestRouteBlock:

    @severity(Level.NORMAL)
    @tag("UI", "smoke", "regress", "routes")
    @allure.title("При вводе двух разных адресов отображается блок выбора маршрута")
    def test_route_block_visible_with_different_addresses(self, main_page_with_route):
        assert main_page_with_route.is_route_block_visible()

    @severity(Level.NORMAL)
    @tag("UI", "smoke", "regress", "routes")
    @allure.title("При вводе одинакового адреса отображается текст 'Авто Бесплатно' и 'В пути 0 мин.'")
    def test_route_text_with_same_address(self, main_page):
        main_page.add_two_address(TaxiData.addresses.LOCATION_1, TaxiData.addresses.LOCATION_1)
        actual_text = main_page.get_route_info_text()
        assert actual_text == list(TaxiData.route.SAME_ADDRESS_TEXT), (
            f"Ожидался текст {TaxiData.route.SAME_ADDRESS_TEXT}, получен {actual_text}"
        )
