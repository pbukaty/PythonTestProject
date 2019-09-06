from appium import webdriver


class Driver:

    def __init__(self):
        self.desire_caps = {
            'platformName': 'Android',
            'deviceName': 'Mi_A2',
            'appPackage': 'by.st.drivepay',
            'appActivity': 'by.st.dp.activities.authorization.AuthorizationActivity'
        }

        self.appiumDriver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", self.desire_caps)
        self.appiumDriver.implicitly_wait(10)
