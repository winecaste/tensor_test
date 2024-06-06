import os

from utils.constants import download_dir
from utils.constants import USER_REGION, KAMCHATKA_PARTIAL_URL, KAMCHATKA_REGION
from utils.locators import SbisPageLocators, TenzorPageLocators
from pages.base_page import BasePage

from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urlparse
import re


class SbisPage(BasePage):
    def go_to_contacts_page(self):
        """Go to the contacts page"""
        assert self.is_element_present(
            *SbisPageLocators.CONTACTS_LINK
        ), "Contacts link is not presented"
        contacts = self.driver.find_element(*SbisPageLocators.CONTACTS_LINK)
        contacts.click()

    def click_tensor_banner(self):
        """Click on the Tensor banner"""
        assert self.is_element_present(
            *TenzorPageLocators.TENSOR_BANNER
        ), "Tensor banner is not presented"
        tensor_banner = self.driver_wait.until(
            EC.element_to_be_clickable(TenzorPageLocators.TENSOR_BANNER)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoViewIfNeeded(true);", tensor_banner
        )
        tensor_banner.click()

    def check_user_region(self):
        """Check user region"""
        region = self.driver.find_element(*SbisPageLocators.REGION)
        assert USER_REGION == region.text, "The user's region does not match"

    def check_user_region_partners(self):
        """Check user region partners"""
        assert self.is_element_present(
            *SbisPageLocators.SBIS_PARTNERS
        ), "The list of partners is missing"
        partners = self.driver.find_elements(*SbisPageLocators.SBIS_PARTNERS)
        assert len(partners) > 0

    def click_region_window(self):
        """Click on the regions window"""
        self.driver_wait.until(
            EC.presence_of_element_located(SbisPageLocators.REGION)
        ).click()

    def change_region(self):
        """Changing the region"""
        self.driver_wait.until(
            EC.visibility_of_element_located(SbisPageLocators.REGION_HEADER)
        )
        assert self.is_element_present(
            *SbisPageLocators.REGION_HEADER
        ), "The header is missing"
        kamchatka_region = self.driver_wait.until(
            EC.element_to_be_clickable(SbisPageLocators.KAMCHATSKIY_REGION)
        )
        kamchatka_region.click()
        self.driver_wait.until(EC.url_contains(KAMCHATKA_PARTIAL_URL))

    def check_url_and_title(self):
        """Checking the url and title"""
        assert (
            KAMCHATKA_PARTIAL_URL in self.driver.current_url
        ), "This region is not in the url"
        assert KAMCHATKA_REGION in self.driver.title, "This region is not in the title"

    def check_new_partners(self, user_region_partners_list):
        """Checking that the partners have been changed"""

        new_region_partners_list = self.driver.find_element(
            *SbisPageLocators.SBIS_PARTNERS
        )
        assert (
            user_region_partners_list != new_region_partners_list
        ), "The list of partners has not changed"

    def go_to_download_page(self):
        """Go to the download page"""
        assert self.is_element_present(
            *SbisPageLocators.DOWNLOAD_LINK
        ), "Download link is missing"
        download_link = self.driver_wait.until(
            EC.element_to_be_clickable(SbisPageLocators.DOWNLOAD_LINK)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoViewIfNeeded(true);", download_link
        )
        download_link.click()

    def click_button_plugin(self):
        """Click on the 'СБИС Плагин'"""
        plugin_button = self.driver_wait.until(
            EC.element_to_be_clickable(SbisPageLocators.PLAGIN_BUTTON)
        )
        assert self.is_element_present(
            *SbisPageLocators.PLAGIN_BUTTON
        ), "Plugin button is missing"
        plugin_button.click()

    def download_plugin(self):
        """Download plugin in directory"""
        plugin = self.driver.find_element(*SbisPageLocators.PLAGIN_DOWNLOAD_LINK)
        plugin.send_keys(download_dir)
        plugin.click()
        self.driver_wait.until(
            lambda d: os.path.exists(
                os.path.join(download_dir, "sbisplugin-setup-web.exe")
            )
        )
        return plugin

    def check_plugin(self, plugin):
        """Checking if the file has been downloaded"""
        attribute_name = plugin.get_attribute("href")
        parsed_url = urlparse(attribute_name)
        path = parsed_url.path
        site_filename = os.path.basename(path)

        downloaded_file = os.path.join(download_dir, site_filename)
        assert os.path.exists(downloaded_file), "The file has not been downloaded"
        return downloaded_file

    def check_file_sizes(self, site_plugin, download_plugin):
        """Comparing the size of the downloaded file and the file on the site"""
        file_info = site_plugin.text
        site_file_size = float(re.search(r"[\d.]+", file_info).group())
        downloaded_file_size = self.get_file_size(download_plugin)
        assert site_file_size == downloaded_file_size, "The file sizes do not match"

    def get_file_size(self, file_path):
        return round(os.path.getsize(file_path) / (1024 * 1024), 2)

    def delete_downloaded_plugin(self, downloaded_file):
        if os.path.exists(downloaded_file):
            os.remove(downloaded_file)
        assert not os.path.exists(downloaded_file), "The file has not been deleted"
