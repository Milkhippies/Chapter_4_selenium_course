from .base_page import BasePage
from .locators import LoginPageLocators


# link = http://selenium1py.pythonanywhere.com/ru/accounts/login/

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "'login' not in current url"

    def should_be_login_form(self):
        loginMail = self.browser.find_element(*LoginPageLocators.LOGIN_MAIL)
        loginPassword = self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD)
        loginButton = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        loginButton.click()
        assert True, "ошибка в форме логина"

    def should_be_register_form(self):
        registrationMail = self.browser.find_element(*LoginPageLocators.REGISTRATION_MAIL)
        registrationPassword = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        registrationConfirmPassword = self.browser.find_element(*LoginPageLocators.REGISTRATION_CONFIRM)
        registrationButton = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        registrationButton.click()
        assert True, "ошибка в форме регистрации"
