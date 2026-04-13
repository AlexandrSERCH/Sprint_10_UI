BASE_URL = "https://ez-route.stand.praktikum-services.ru"

URLS = {
    "main_page": f"{BASE_URL}/",
}

SHORT_WAIT: int = 5
LONG_WAIT: int = 80


def main_page_url() -> str:
    return URLS["main_page"]
