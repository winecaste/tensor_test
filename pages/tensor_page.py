from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

from utils.constants import ABOUT_LINK
from utils.locators import TenzorPageLocators


class TensorPage(BasePage):
    def check_block(self):
        block = self.driver_wait.until(
            EC.presence_of_element_located(TenzorPageLocators.TENSOR_BLOCK)
        )
        self.driver.execute_script("arguments[0].scrollIntoViewIfNeeded(true);", block)
        assert self.is_element_present(
            *TenzorPageLocators.TENSOR_BLOCK
        ), "Tensor block is not presented"

    def go_to_details(self):
        about = self.driver_wait.until(
            EC.element_to_be_clickable(TenzorPageLocators.TENSOR_ABOUT_LINK)
        )
        about.click()
        assert (
            ABOUT_LINK == self.driver.current_url
        ), 'Page "https://tensor.ru/about" does not open'

    def check_working_section_photos(self):
        images = self.driver_wait.until(
            EC.presence_of_all_elements_located(TenzorPageLocators.TENSOR_ABOUT_PHOTO)
        )
        sizes = [(img.size["width"], img.size["height"]) for img in images]
        return all(size == sizes[0] for size in sizes)
