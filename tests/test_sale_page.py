import pytest
import allure

from pages.helper.text_to_check import MAIN_SALE_WOMAN_INFO, MAIN_SALE_WOMAN_BUTTON, \
    MAIN_SALE_WOMAN_TITLE, WOMAN_SALE_TITLE


@allure.feature('Tests for "Sale Page" page')
class TestSalePage:
    @pytest.mark.fast_smoke
    @allure.story("Display All Sales Blocks")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_all_sales_blocks_are_displayed(self, sales_page):
        with allure.step("Open the Sales Page"):
            sales_page.open_by_url()
        with allure.step("Check that all sales cards are displayed"):
            sales_page.check_all_sales_cards_are_displayed()

    @pytest.mark.smoke
    @allure.story("Main Sale Card UI Validation")
    @allure.severity(allure.severity_level.NORMAL)
    def test_main_sales_card_ui(self, sales_page):
        with allure.step("Open the Sales Page"):
            sales_page.open_by_url()
        with allure.step("Find all elements inside the main sale card"):
            sales_page.find_all_elements_inside_main_sale_card()
        with allure.step("Check if the text inside the main sale card is correct"):
            sales_page.check_if_text_inside_main_sale_card_is_correct(MAIN_SALE_WOMAN_INFO,
                                                                      MAIN_SALE_WOMAN_TITLE, MAIN_SALE_WOMAN_BUTTON)

    @pytest.mark.full_test
    @allure.story("Open Main Sale Screen via Clicking on Button")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_open_main_sale_screen_via_clicking_on_button(self, sales_page, women_sale_page):
        with allure.step("Open the Sales Page and get the current URL"):
            sales_url = sales_page.open_by_url()
        with allure.step("Click on 'Show Main Deal' button"):
            sales_page.click_on_show_main_deal_button()
        with allure.step("Check if the URL has changed after the click"):
            women_sale_page.check_url_was_changed(sales_url)
        with allure.step("Check if the page title of the women sale page is displayed"):
            women_sale_page.check_if_page_title_is_displayed(WOMAN_SALE_TITLE)
