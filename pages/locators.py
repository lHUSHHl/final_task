from selenium.webdriver.common.by import By


class LoginPanelLocators:
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class AddProduct:
    ADD_TO_BASKET_FORM = (By.CSS_SELECTOR, "#add_to_basket_form")
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRICE = (By.CSS_SELECTOR, "div.product_main .price_color")
    TITLE = (By.CSS_SELECTOR, "div.product_main h1")
    MESSAGE_ABOUT_ADD = (By.CSS_SELECTOR, "div.alertinner")
    BASKET_TOTAL = (By.CSS_SELECTOR, "div.alert.alert-info strong")

