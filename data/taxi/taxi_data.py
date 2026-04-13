from dataclasses import dataclass
from typing import List, Tuple


@dataclass(frozen=True)
class Addresses:
    LOCATION_1: str = "Хамовнический вал, 34"
    LOCATION_2: str = "Зубовский бульвар, 37"


@dataclass(frozen=True)
class TaxiTariffs:
    TITLES: Tuple[str, ...] = (
        "Рабочий",
        "Сонный",
        "Отпускной",
        "Разговорчивый",
        "Утешительный",
        "Глянцевый",
    )
    DESCRIPTIONS: Tuple[str, ...] = (
        "Рабочий - Для деловых особ, которых отвлекают",
        "Сонный - Для тех, кто не выспался",
        "Отпускной - Если пришла пора отдохнуть",
        "Разговорчивый - Если мысли не выходят из головы",
        "Утешительный - Если хочется свернуться калачиком",
        "Глянцевый - Если нужно блистать",
    )

    def as_parametrize_pairs(self) -> List[Tuple[str, str]]:
        return list(zip(self.TITLES, self.DESCRIPTIONS))


@dataclass(frozen=True)
class RouteExpected:
    SAME_ADDRESS_TEXT: Tuple[str, str] = ("Авто Бесплатно", "В пути 0 мин.")
    ACTIVE_TAB: str = "Оптимальный"


class OrderBlock:
    FIELDS: Tuple[str, ...] = (
        "Телефон",
        "Способ оплаты",
        "Комментарий водителю",
        "Требования к заказу",
        "Заказ тарифа Такси",
    )


@dataclass(frozen=True)
class Drivers:
    NAMES: Tuple[str, ...] = ("Алексей", "Петр", "Михаил", "Григорий", "Аркадий", "Евгений")


class TaxiData:
    addresses = Addresses()
    tariffs = TaxiTariffs()
    route = RouteExpected()
    order_block = OrderBlock()
    drivers = Drivers()
