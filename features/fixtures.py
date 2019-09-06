from behave import fixture

from settings.driver import Driver


@fixture
def setup_driver(context):
    try:
        driver = Driver().appiumDriver
        context.driver = driver
        yield driver
    finally:
        driver.quit()
