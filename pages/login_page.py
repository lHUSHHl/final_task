from .base_page import BasePage
from .locators import LoginPanelLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        email_form = self.browser.find_element(
            *LoginPanelLocators.EMAIL_ADDRESS)
        email_form.send_keys(email)

        password_form = self.browser.find_element(
            *LoginPanelLocators.PASSWORD)
        password_form.send_keys(password)

        confirm_password_form = self.browser.find_element(
            *LoginPanelLocators.CONFIRM_PASSWORD)
        confirm_password_form.send_keys(password)

        registration_button = self.browser.find_element(
            *LoginPanelLocators.BUTTON_REGISTRATION)
        registration_button.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "login is not in the url"

    def should_be_login_form(self):
        self.is_element_present(
            *LoginPanelLocators.LOGIN_FORM), \
                    "login form is not presented"

    def should_be_register_form(self):
        self.is_element_present(
            *LoginPanelLocators.REGISTRATION_FORM), \
                    "registration form is not presented"
