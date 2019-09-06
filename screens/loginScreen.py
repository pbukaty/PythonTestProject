from elements.element import Element


class LoginScreen:

    PHONE_NUMBER_TEXTBOX_ID = "vLogin"
    PASSWORD_TEXTBOX_ID = "vPassword"
    LOGIN_BUTTON = "btnLogin"
    USE_FAST_CHECKBOX = "vUseFastLogin"

    def __init__(self, driver):
        self.element = Element(driver)

    def get_phone_number_textbox_enabled_state(self):
        return self.element.get_element_by_id(LoginScreen.PHONE_NUMBER_TEXTBOX_ID).get_attribute("enabled")

    def get_password_textbox_enabled_state(self):
        return self.element.get_element_by_id(LoginScreen.PASSWORD_TEXTBOX_ID).get_attribute("enabled")

    def type_phone_number(self, number):
        phone_number_textbox = self.element.get_element_by_id(LoginScreen.PHONE_NUMBER_TEXTBOX_ID)
        phone_number_textbox.clear()
        phone_number_textbox.send_keys(number)

    def type_password(self, password):
        password_textbox = self.element.get_element_by_id(LoginScreen.PASSWORD_TEXTBOX_ID)
        password_textbox.clear()
        password_textbox.send_keys(password)

    def click_login_button(self):
        login_button = self.element.get_element_by_id(LoginScreen.LOGIN_BUTTON)
        login_button.click()

    def set_fast_login_checkbox_state(self, state):
        fast_login_checkbox = self.element.get_element_by_id(LoginScreen.USE_FAST_CHECKBOX)
        current_state = fast_login_checkbox.get_attribute("checked")
        if current_state != state:
            fast_login_checkbox.click()
