from behave import *


class Steps:

    @given('Login screen is loaded')
    def step_impl(context):
        assert context.login_screen.get_phone_number_textbox_enabled_state() == 'true'
        assert context.login_screen.get_password_textbox_enabled_state() == 'true'

    @when('type mobile phone')
    def step_impl(context):
        context.login_screen.type_phone_number(context.phoneNumber)

    @when('type password')
    def step_impl(context):
        context.login_screen.type_password(context.password)

    @when('set fast login checkbox state to "{state}"')
    def step_impl(context, state):
        context.login_screen.set_fast_login_checkbox_state(state)

    @when('tap Login button')
    def step_impl(context):
        context.login_screen.click_login_button()

    @then('Main screen is opened')
    def step_impl(context):
        assert context.main_screen.get_zoom_in_button_enabled_state() == 'true'
        assert context.main_screen.get_zoom_out_button_enabled_state() == 'true'
        assert context.main_screen.get_focus_to_user_button_enabled_state() == 'true'
