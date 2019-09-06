from elements.element import Element


class MainScreen:

    ZOOM_IN_BUTTON = "vZoomIn"
    ZOOM_OUT_BUTTON = "vZoomOut"
    FOCUS_TO_USER_BUTTON = "vFocusToUser"

    def __init__(self, driver):
        self.element = Element(driver)
        self.driver = driver

    def get_zoom_in_button_enabled_state(self):
        return self.element.get_element_by_id(MainScreen.ZOOM_IN_BUTTON).get_attribute("enabled")

    def get_zoom_out_button_enabled_state(self):
        return self.element.get_element_by_id(MainScreen.ZOOM_OUT_BUTTON).get_attribute("enabled")

    def get_focus_to_user_button_enabled_state(self):
        return self.element.get_element_by_id(MainScreen.FOCUS_TO_USER_BUTTON).get_attribute("enabled")
