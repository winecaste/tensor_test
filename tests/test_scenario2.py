from pages.sbis_page import SbisPage
from utils.constants import SBIS_LINK

from loguru import logger


def test_scenario_two(driver):
    """Checking the second scenario"""
    logger.info("Init SbisPage")
    sbis_page = SbisPage(driver, SBIS_LINK)
    sbis_page.open()

    logger.info("Go to the contact page")
    sbis_page.go_to_contacts_page()

    logger.info("Check user region")
    sbis_page.check_user_region()

    logger.info("Check user region partners")
    user_region_partners = sbis_page.check_user_region_partners()

    logger.info("Click on the regions window")
    sbis_page.click_region_window()

    logger.info("Changing the region")
    sbis_page.change_region()

    logger.info("Checking the url and title")
    sbis_page.check_url_and_title()

    logger.info("Checking that the partners have been changed")
    sbis_page.check_new_partners(user_region_partners)
