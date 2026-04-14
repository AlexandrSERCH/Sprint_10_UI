from selenium.webdriver.common.by import By


class MainPageLocators:

    # Поля ввода адреса
    FROM_FIELD = (By.XPATH, '//input[@id="from"]')
    TO_FIELD = (By.XPATH, '//input[@id="to"]')

    # Точки маршрута на карте
    FROM_DOT = (By.XPATH, '//ymaps[contains(@class,"ff3333")]')
    TO_DOT = (By.XPATH, '//ymaps[contains(@class,"4296ea")]')

    # Вкладки и блок выбора маршрута
    OPTIMA = (By.XPATH, '//div[text()="Оптимальный"]')
    QUICK = (By.XPATH, '//div[text()="Быстрый"]')
    OWN = (By.XPATH, '//div[text()="Свой"]')
    ACTIVE_TAB = (By.XPATH, '//div[@class="mode active"]')
    TYPE_AND_PRICE_DELIVERY = (By.XPATH, '//div[@class="text"]')
    TRAVEL_TIME = (By.XPATH, '//div[@class="duration"]')
    CALL_TAXI = (By.XPATH, '//button[text()="Вызвать такси"]')
    CONFIRMATION = (By.XPATH, '//button[text()="Забронировать"]')

    # Типы транспорта в маршруте Свой
    TYPE_WALK = (By.XPATH, '//img[contains(@src,"walk")]')
    TYPE_TAXI = (By.XPATH, '//img[contains(@src,"taxi")]')
    TYPE_BIKE = (By.XPATH, '//img[contains(@src,"bike")]')
    TYPE_SCOOTER = (By.XPATH, '//img[contains(@src,"scooter")]')
    TYPE_DRIVE = (By.XPATH, '//img[contains(@src,"drive")]')
    TYPE_CAR = (By.XPATH, '//div/img[contains(@src,"car.")]')

    # Группы локаторов для итерации
    LOCATORS_OF_CHOICE = (OPTIMA, QUICK, TYPE_AND_PRICE_DELIVERY, TRAVEL_TIME, CALL_TAXI)
    LOCATORS_OF_TRANSPORT = (TYPE_WALK, TYPE_TAXI, TYPE_BIKE, TYPE_SCOOTER, TYPE_DRIVE, TYPE_CAR)
