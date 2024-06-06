from selenium.webdriver.common.by import By


class SbisPageLocators:
    """Класс локаторов для SbisPage"""

    CONTACTS_LINK = (By.CSS_SELECTOR, '[href="/contacts"]')
    REGION = (By.CSS_SELECTOR, ".sbis_ru-Region-Chooser__text.sbis_ru-link")
    SBIS_PARTNERS = (By.CSS_SELECTOR, ".sbisru-Contacts-List--ellipsis")
    REGION_HEADER = (By.CSS_SELECTOR, ".sbis_ru-Region-Panel__header")

    KAMCHATSKIY_REGION = (
        By.CSS_SELECTOR,
        ".sbis_ru-Region-Panel__list-l .sbis_ru-Region-Panel__item:nth-child(43)",
    )
    DOWNLOAD_LINK = (By.CSS_SELECTOR, ".sbisru-Footer__link[href='/download']")
    PLAGIN_BUTTON = (
        By.XPATH,
        '//div[@class="sbis_ru-VerticalTabs__left"]/div[contains(@sbisname, "TabButtons")]/div[2]',
    )
    PLAGIN_DOWNLOAD_LINK = (By.XPATH, '//a[contains(text(), "Скачать (Exe")]')


class TenzorPageLocators:
    """Класс локаторов для TenzorPage"""

    TENSOR_LINK = (By.CSS_SELECTOR, '[href="https://tensor.ru/"]')
    TENSOR_BANNER = (By.XPATH, "//a[@href='https://tensor.ru/']")
    TENSOR_BLOCK = (
        By.CSS_SELECTOR,
        "[class='tensor_ru-Index__block4-content tensor_ru-Index__card']",
    )
    TENSOR_ABOUT_LINK = (By.XPATH, "//a[@href='/about' and text()='Подробнее']")
    TENSOR_ABOUT_PHOTO = (By.CSS_SELECTOR, ".tensor_ru-About__block3-image-filter")
