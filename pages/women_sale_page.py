from pages.base_page import BasePage
from pages.locators import women_sale


class WomenSale(BasePage):
    page_url = 'https://magento.softwaretestingboard.com/promotions/women-sale.html'

    def check_if_page_title_is_displayed(self, expected_title_text):
        title = self.find_element(women_sale.WOMEN_SALE_TITLE)
        assert title.text == expected_title_text
