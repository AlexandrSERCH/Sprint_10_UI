import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import constants


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, constants.SHORT_WAIT)
        self.long_wait = WebDriverWait(self.driver, constants.LONG_WAIT)

    @allure.step("Открыть страницу по ссылке: {url}")
    def _open_page(self, url: str) -> None:
        self.driver.get(url)

    @allure.step("Нажать на элемент по локатору: {locator}")
    def _click(self, locator) -> None:
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step("Ввести текст: '{text}' в поле по локатору: {locator}")
    def _send_keys(self, locator, text: str) -> None:
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.clear()
        element.send_keys(text)

    @allure.step("Получить текст элемента по локатору: {locator}")
    def _get_text(self, locator) -> str:
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    @allure.step("Получить текущий URL")
    def _get_current_url(self) -> str:
        return self.driver.current_url

    @allure.step("Проверить видимость элемента по локатору: {locator}")
    def _is_visible(self, locator) -> None:
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"Элемент не отображается: {locator}")

    @allure.step("Найти элемент с ожиданием по локатору: {locator}")
    def _find_element(self, locator) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Найти все элементы с ожиданием по локатору: {locator}")
    def _find_elements(self, locator) -> list:
        self.wait.until(EC.presence_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    @allure.step("Ожидать скрытия элемента: {locator}")
    def _wait_invisible(self, locator) -> WebElement:
        return self.wait.until(EC.invisibility_of_element_located(locator))

    @allure.step("Длительное ожидание скрытия элемента: {locator}")
    def _long_wait_invisible(self, locator) -> WebElement:
        return self.long_wait.until(EC.invisibility_of_element_located(locator))

    @allure.step("Навести курсор на элемент")
    def _hover(self, element: WebElement) -> None:
        ActionChains(self.driver).move_to_element(element).perform()

    @allure.step("Проскроллить до элемента: {locator}")
    def _scroll_to(self, locator) -> None:
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Проверить видимость элемента: {locator}")
    def _check_visible(self, locator) -> bool:
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    @allure.step("Проверить кликабельность элемента: {locator}")
    def _is_clickable(self, locator) -> bool:
        try:
            self.wait.until(EC.element_to_be_clickable(locator))
            return True
        except TimeoutException:
            return False

    @allure.step("Получить текст двух элементов")
    def _get_texts(self, locator_1, locator_2) -> list:
        return [
            self._get_text(locator_1),
            self._get_text(locator_2),
        ]