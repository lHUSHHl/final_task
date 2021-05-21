from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_form(self):
        self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_FORM), \
            "add form is not presented"

    def add_to_basket(self):
        add_button = self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    def should_be_message_about_add(self):
        self.is_element_present(*ProductPageLocators.PRODUCT_NAME), \
            "product name is not presented"

        self.is_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADD), \
            "message is not presented"

        product_name = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME).text
        message_about_add = self.browser.find_element(
            *ProductPageLocators.MESSAGE_ABOUT_ADD).text

        assert product_name == message_about_add, f'expected {product_name} in message, ' \
                                                  f'received {message_about_add}'

    def should_be_price(self):
        self.is_element_present(*ProductPageLocators.PRICE), \
            "price is not presented"

        self.is_element_present(*ProductPageLocators.BASKET_TOTAL), \
            "basket total price is not presented"

        price_on_add_form = self.browser.find_element(
            *ProductPageLocators.PRICE).text
        basket_total_price = self.browser.find_element(
            *ProductPageLocators.BASKET_TOTAL).text

        assert price_on_add_form == basket_total_price, \
            f'basket total price should be {price_on_add_form}'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.MESSAGE_ABOUT_ADD), \
            "success message is presented, but should not be"

    def should_disappear(self):
        assert self.is_disappear(
            *ProductPageLocators.MESSAGE_ABOUT_ADD), \
            "success message is presented, but has not disappeared"
