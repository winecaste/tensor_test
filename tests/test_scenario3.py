import os

from utils.constants import download_dir
from pages.sbis_page import SbisPage
from utils.constants import SBIS_LINK

from loguru import logger


def test_scenario_three(driver):
    """Checking the third scenario"""
    logger.info("Init SbisPage")
    sbis_page = SbisPage(driver, SBIS_LINK)
    sbis_page.open()

    logger.info("Go to the page 'Скачать локальные версии'")
    sbis_page.go_to_download_page()

    logger.info("Click on the 'СБИС Плагин'")
    sbis_page.click_button_plugin()

    logger.info("Download plugin")
    plugin = sbis_page.download_plugin()

    logger.info("Checking if the file has been downloaded")
    plagin_path = sbis_page.check_plugin(plugin)
    downloaded_plugin = os.path.join(download_dir, "sbisplugin-setup-web.exe")

    logger.info("Comparing the size of the downloaded file and the file on the site")
    sbis_page.check_file_sizes(plugin, downloaded_plugin)

    logger.info("Delete the file after all checks")
    sbis_page.delete_downloaded_plugin(plagin_path)
