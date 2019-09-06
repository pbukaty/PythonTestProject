from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Element:
    def __init__(self, driver):
        self.driver = driver

    def get_element_by_id(self, id):
        try:
            return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((MobileBy.ID, id)))
        except:
            print("Element with id = '" + id + "' cannot be found")
