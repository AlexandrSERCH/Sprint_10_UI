# Sprint 10 — UI автотесты

Автотесты для веб-приложения [EZ-Route](https://ez-route.stand.praktikum-services.ru) (сервис построения маршрутов и вызова такси).

## Стек

| Инструмент | Версия | Назначение |
|---|---|---|
| Python | ≥ 3.12 | язык |
| pytest | 9.0.2 | фреймворк |
| selenium | 4.18.1 | браузерная автоматизация |
| allure-pytest | 2.13.5 | отчёты |
| pytest-xdist | 3.8.0 | параллельный запуск |
| webdriver-manager | 4.0.1 | управление драйвером |

## Структура проекта

```
Sprint_10_UI/
├── conftest.py                     # фикстуры: browser, main_page, call_taxi_page и цепочки
├── constants.py                    # BASE_URL, таймауты ожидания
│
├── locators/
│   ├── main_page_locators.py       # локаторы главной страницы
│   └── call_taxi_page_locators.py  # локаторы формы заказа такси
│
├── pages/
│   ├── base_page.py                # базовые методы Selenium (click, send_keys, wait и т.д.)
│   ├── main_page.py                # POM: главная страница
│   └── call_taxi_page.py           # POM: форма заказа такси + окно поиска водителя
│
├── data/
│   └── taxi/
│       └── taxi_data.py            # тестовые данные (адреса, тарифы, водители)
│
├── tests/
│   ├── test_route_block.py         # блок выбора маршрута
│   ├── test_route_drawing.py       # отображение маршрута на карте
│   ├── test_taxi_preparation.py    # переключение вкладок, кнопки
│   ├── test_taxi_order.py          # тарифы и поля формы заказа
│   └── test_taxi_flow.py           # поиск машины и финальное окно водителя
│
└── utils/
    ├── attach.py                   # прикрепление скриншота к allure-отчёту
    └── markers.py                  # хелперы @tag и @severity (allure + pytest.mark одновременно)
```

## Установка

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -e .
```

> Браузер Chrome должен быть установлен. Драйвер подтягивается автоматически через `webdriver-manager`.

## Запуск тестов

```bash
# все тесты (параллельно, allure-результаты в ./allure-result)
pytest

# только smoke
pytest -m smoke

# только тесты такси
pytest -m taxi

# только тесты маршрутов
pytest -m routes

# без параллелизма (для отладки)
pytest -n0
```

## Allure-отчёт

```bash
allure serve allure-result
```

## Известные баги (xfail)

| Тест | Причина |
|---|---|
| `test_tariff_description_matches_spec[Сонный]` | Отображается описание от тарифа "Разговорчивый" |
| `test_tariff_description_matches_spec[Разговорчивый]` | Отображается описание от тарифа "Сонный" |
| `test_cancel_button_closes_modal` | Кнопка "Отменить" не кликабельна |
