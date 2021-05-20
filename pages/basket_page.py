from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_a_message_about_an_empty(self):
        self.is_element_present(
            *BasketPageLocators.MESSAGE_ABOUT_EMPTY), \
        "message is not presented"

    def basket_is_empty(self):
        assert self.is_not_element_present(
            *BasketPageLocators.ITEMS_IN_BASKET), \
            "basket is not empty, but should be"
