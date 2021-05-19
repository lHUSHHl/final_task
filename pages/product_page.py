from .base_page import BasePage
from .locators import AddProduct


class ProductPage(BasePage):
    def should_be_add_form(self):
        self.is_element_present(*AddProduct.ADD_TO_BASKET_FORM), \
        "add form is not presented"

    def add_to_basket(self):
        add_button = self.browser.find_element(*AddProduct.ADD_TO_BASKET_BUTTON)
        add_button.click()

    def should_be_message_about_add(self):
        self.is_element_present(*AddProduct.TITLE), \
        "product name is not presented"

        self.is_element_present(*AddProduct.MESSAGE_ABOUT_ADD), \
        "message is not presented"

        product_name = self.browser.find_element(*AddProduct.TITLE).text
        message_about_add = self.browser.find_element(*AddProduct.MESSAGE_ABOUT_ADD).text

        assert product_name in message_about_add, f'expected {product_name} in message'

    def should_be_price(self):
        self.is_element_present(*AddProduct.PRICE), \
        "price is not presented"

        self.is_element_present(*AddProduct.BASKET_TOTAL), \
        "basket total price is not presented"

        price_on_add_form = self.browser.find_element(*AddProduct.PRICE).text
        basket_total_price = self.browser.find_element(*AddProduct.BASKET_TOTAL).text

        assert price_on_add_form == basket_total_price, f'basket total price should be {price_on_add_form}'