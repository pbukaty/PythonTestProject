import subprocess

from behave.fixture import use_fixture
from features.fixtures import setup_driver
from screens.loginScreen import LoginScreen
from screens.mainScreen import MainScreen
from utils.jsonParser import JsonParser


def before_all(context):
    parser = JsonParser()
    params = parser.parse("config.json")
    app_package = params['AppPackage']
    context.phoneNumber = params['PhoneNumber']
    context.password = params['Password']

    use_fixture(setup_driver, context)
    subprocess.call("adb shell pm grant " + app_package + " android.permission.ACCESS_COARSE_LOCATION", shell=False)


def before_tag(context, tag):
    if tag == "login":
        context.login_screen = LoginScreen(context.driver)
        context.main_screen = MainScreen(context.driver)
