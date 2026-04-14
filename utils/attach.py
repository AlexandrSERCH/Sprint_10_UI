import allure
from allure_commons.types import AttachmentType


def attach_screenshot(driver, name="Скриншот") -> None:
    try:
        png = driver.get_screenshot_as_png()
    except Exception:
        return
    allure.attach(png, name=name, attachment_type=AttachmentType.PNG)
