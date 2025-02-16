from pages.locators import account_page as account
from pages.base_page import BasePage


class AccountPage(BasePage):
    page_url = 'https://magento.softwaretestingboard.com/customer/account/'

    def check_success_message_appeared(self, expected_error_message):
        success_message = self.find_element(account.SUCCESS_MESSAGE)
        assert success_message.text == expected_error_message
