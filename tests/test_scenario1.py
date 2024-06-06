from pages.sbis_page import SbisPage
from pages.tensor_page import TensorPage
from utils.constants import SBIS_LINK, TENZOR_LINK

from loguru import logger


def test_scenario_one(driver):
    """Checking the first scenario"""
    logger.info("Init SbisPage")
    sbis_page = SbisPage(driver, SBIS_LINK)
    sbis_page.open()

    logger.info("Go to the contact page")
    sbis_page.go_to_contacts_page()

    logger.info("Click on the Tensor banner")
    sbis_page.click_tensor_banner()

    logger.info("Switching to a new tab")
    driver.switch_to.window(driver.window_handles[-1])

    logger.info("Init TensorPage")
    tensor_page = TensorPage(driver, TENZOR_LINK)

    logger.info("Checking for block 'Сила в людях' availability")
    tensor_page.check_block()

    logger.info("Click on the 'about'")
    tensor_page.go_to_details()

    logger.info(f"Checking the photo size")
    tensor_page.check_working_section_photos()
