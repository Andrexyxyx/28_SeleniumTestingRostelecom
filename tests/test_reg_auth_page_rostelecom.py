from pages.reg_page_rostelecom import RegPage
from pages.config_rostelecom import valid_firstname, invalid_firstname, valid_lastname, invalid_lastname, \
    default_region, valid_email, invalid_email, valid_phone, invalid_phone, valid_password, \
    invalid_password1, invalid_password2, invalid_password3, valid_confirm_password, invalid_confirm_password, \
    reg_email, empty_firstname, empty_lastname, empty_phone, empty_email, empty_password, auth_email_valid,\
    auth_password_valid, auth_password_incorrect, auth_email_incorrect
import time
from pages.confirm_reg_page_rostelecom import ConfirmRegPage
from pages.auth_page_rostelecom import AuthPage

import time
from termcolor import colored

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys



# Команда для запуска тестов
# python -m pytest -v --driver Chrome --driver-path C:/Documents/chromedriver.exe tests/test_reg_auth_page_rostelecom.py

def test1_firstname_field_valid(web_browser):
    """Проверка валидации поля 'Имя' при вводе буквенных значений на странице регистрации. Позитивный сценарий"""
    page = RegPage(web_browser)
    page.registration_button.click()
    page.firstname_field.send_keys(valid_firstname)
    page.lastname_field.click()

    assert 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.' not in page.error_firstname.get_text()
    assert not page.error_firstname.is_visible()


def test2_firstname_field_invalid(web_browser):
    """Проверка валидации поля 'Имя' при вводе буквенных значений на странице регистрации. Негативный сценарий"""
    page = RegPage(web_browser)
    page.registration_button.click()
    page.firstname_field.send_keys(invalid_firstname)
    page.lastname_field.click()

    assert 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.' in page.error_firstname.get_text()
    assert page.error_firstname.is_visible()


def test3_lastname_field_valid(web_browser):
    """Проверка валидации поля 'Фамилия' при вводе буквенных значений на странице регистрации. Позитивный сценарий"""
    page = RegPage(web_browser)
    page.registration_button.click()
    page.lastname_field.send_keys(valid_lastname)
    page.firstname_field.click()

    assert 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.' not in page.error_lastname.get_text()
    assert not page.error_lastname.is_visible()


def test4_lastname_field_invalid(web_browser):
    """Проверка валидации поля 'Фамилия' при вводе буквенных значений на странице регистрации. Негативный сценарий"""
    page = RegPage(web_browser)
    page.registration_button.click()
    page.lastname_field.send_keys(invalid_lastname)
    page.firstname_field.click()

    assert 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.' in page.error_lastname.get_text()
    assert page.error_lastname.is_visible()


def test5_region_field_default(web_browser):
    """Проверка значения по умолчанию в выпадающем списке поля 'Регион'на странице регистрации. Позитивный
     сценарий"""
    page = RegPage(web_browser)
    page.registration_button.click()

    assert page.region_field.get_attribute('value') == default_region


def test6_email_phone_field_valid_email(web_browser):
    """Проверка валидации поля 'Email или мобильный телефон' при вводе email в требуемом формате на странице
    регистрации. Позитивный сценарий"""
    page = RegPage(web_browser)
    page.registration_button.click()
    page.email_phone_field.send_keys(valid_email)
    page.firstname_field.click()

    assert 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru' not in page.error_email_phone.get_text()
    assert not page.error_email_phone.is_visible()


def test7_email_phone_field_valid_phone(web_browser):
    """Проверка валидации поля 'Email или мобильный телефон' при вводе номера телефона в требуемом формате
    на странице регистрации. Позитивный сценарий"""
    page = RegPage(web_browser)
    page.registration_button.click()
    page.email_phone_field.send_keys(valid_phone)
    page.firstname_field.click()

    assert 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru' not in page.error_email_phone.get_text()
    assert not page.error_email_phone.is_visible()


def test8_email_phone_field_invalid_email(web_browser):
    """Проверка валидации поля 'Email или мобильный телефон' при вводе email в некорректном формате на странице
    регистрации. Негативный сценарий"""
    page = RegPage(web_browser)
    page.registration_button.click()
    page.email_phone_field.send_keys(invalid_email)
    page.firstname_field.click()

    assert 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru' in page.error_email_phone.get_text()
    assert page.error_email_phone.is_visible()


def test9_email_phone_field_invalid_phone(web_browser):
    """Проверка валидации поля 'Email или мобильный телефон' при вводе номера телефона в некорректном формате
    на странице регистрации. Негативный сценарий"""
    page = RegPage(web_browser)
    page.registration_button.click()
    page.email_phone_field.send_keys(invalid_phone)
    page.firstname_field.click()

    assert 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru' in page.error_email_phone.get_text()
    assert page.error_email_phone.is_visible()


def test10_password_field_valid(web_browser):
    """Проверка валидации поля 'Пароль' при вводе пароля в требуемом формате на странице регистрации.
    Позитивный сценарий"""
    page = RegPage(web_browser)
    page.registration_button.click()
    page.password_field.send_keys(valid_password)
    page.firstname_field.click()

    assert 'Длина пароля должна быть не менее 8 символов' not in page.error_password1.get_text()
    assert 'Пароль должен содержать хотя бы одну заглавную букву' not in page.error_password2.get_text()
    assert 'Пароль должен содержать только латинские буквы' not in page.error_password3.get_text()
    assert not page.error_password1.is_visible()
    assert not page.error_password2.is_visible()
    assert not page.error_password3.is_visible()


def test11_password_field_invalid1(web_browser):
    """Проверка валидации поля 'Пароль' при вводе пароля в некорректном формате (менее 8 символов)
    на странице регистрации. Негативный сценарий"""
    page = RegPage(web_browser)
    page.registration_button.click()
    page.password_field.send_keys(invalid_password1)
    page.firstname_field.click()

    assert 'Длина пароля должна быть не менее 8 символов' in page.error_password1.get_text()
    assert page.error_password1.is_visible()


def test12_password_field_invalid2(web_browser):
    """Проверка валидации поля 'Пароль' при вводе пароля в некорректном формате (без заглавной латинской буквы)
    на странице регистрации. Негативный сценарий"""
    page = RegPage(web_browser)
    page.registration_button.click()
    page.password_field.send_keys(invalid_password2)
    page.firstname_field.click()

    assert 'Пароль должен содержать хотя бы одну заглавную букву' in page.error_password2.get_text()
    assert page.error_password2.is_visible()


def test13_password_field_invalid3(web_browser):
    """Проверка валидации поля 'Пароль' при вводе пароля в некорректном формате (с 1 нелатинской буквой)
    на странице регистрации. Негативный сценарий"""
    page = RegPage(web_browser)
    page.registration_button.click()
    page.password_field.send_keys(invalid_password3)
    page.firstname_field.click()

    assert 'Пароль должен содержать только латинские буквы' in page.error_password3.get_text()
    assert page.error_password3.is_visible()


def test14_confirm_password_field_correct(web_browser):
    """Проверка функции поля 'Подтверждение пароля' по сравнению введенного и продублированного паролей при
    вводе одинаковых паролей на странице регистрации. Позитивный сценарий"""
    page = RegPage(web_browser)
    page.registration_button.click()
    page.password_field.send_keys(valid_password)
    page.confirm_password_field.send_keys(valid_confirm_password)
    page.firstname_field.click()

    assert 'Пароли не совпадают' not in page.error_confirm_password.get_text()
    assert not page.error_confirm_password.is_visible()


def test15_confirm_password_field_incorrect(web_browser):
    """Проверка функции поля 'Подтверждение пароля' по сравнению введенного и продублированного паролей при
    вводе разных паролей на странице регистрации. Негативный сценарий"""
    page = RegPage(web_browser)
    page.registration_button.click()
    page.password_field.send_keys(valid_password)
    page.confirm_password_field.send_keys(invalid_confirm_password)
    page.firstname_field.click()
    page.screenshot('test15.jpg')

    assert 'Пароли не совпадают' in page.error_confirm_password.get_text()
    assert page.error_confirm_password.is_visible()


def test16_success_registration(web_browser):
    """Проверка перехода на страницу подтверждения e-mail после ввода корректной информации о пользователе
    во время регистрации. Позитивный сценарий"""
    page = RegPage(web_browser)
    page.registration_button.click()
    page.firstname_field.send_keys(valid_firstname)
    page.lastname_field.send_keys(valid_lastname)
    page.email_phone_field.send_keys(valid_email)
    page.password_field.send_keys(valid_password)
    page.confirm_password_field.send_keys(valid_confirm_password)
    page.registration_submit_button.click()

    page_confirm = ConfirmRegPage(web_browser)

    assert page_confirm.confirm_email_title
    assert page_confirm.change_email_button
    assert 'openid-connect' in page_confirm.get_current_url()


def test17_unsuccess_registration(web_browser):
    """Проверка перехода на страницу подтверждения e-mail после ввода корректной информации о пользователе
    во время регистрации. Негативный сценарий"""
    page = RegPage(web_browser)
    page.registration_button.click()
    page.firstname_field.send_keys(empty_firstname)
    page.lastname_field.send_keys(empty_lastname)
    page.email_phone_field.send_keys(empty_email)
    page.password_field.send_keys(empty_password)
    page.confirm_password_field.send_keys(empty_password)
    page.registration_submit_button.click()

    assert 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.' in page.error_firstname.get_text()
    assert page.error_firstname.is_visible()

    assert 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.' in page.error_lastname.get_text()
    assert page.error_lastname.is_visible()

    assert 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru' in page.error_email_phone.get_text()
    assert page.error_email_phone.is_visible()

    assert 'Длина пароля должна быть не менее 8 символов' in page.error_password1.get_text()

    assert 'login-actions' in page.get_current_url()


def test18_auth_default_tab(web_browser):
    """Проверка значения по умолчанию выбора типа авторизации (по телефону)"""
    page = AuthPage(web_browser)

    assert 'rt-tab--active' in page.auth_tab_phone_button.get_attribute('className')
    assert 'Телефон' in page.auth_tab_phone_button.get_text()


def test19_auth_success_valid(web_browser):
    """Проверка успешной аутентификации пользователя по адресу email и паролю при вводе валидных данных.
    Позитивный сценарий"""
    page = AuthPage(web_browser)
    page.auth_tab_email_button.click()
    page.username_field.send_keys(auth_email_valid)
    page.password_field.send_keys(auth_password_valid)
    page.auth_button.click()

    assert 'https://b2c.passport.rt.ru/account_b2c/page' in page.get_current_url()

    assert page.title_account_data
    assert 'Учетные данные' in page.title_account_data.get_text()

    assert page.title_security
    assert 'Безопасность' in page.title_security.get_text()

    assert page.title_private_cabinets
    assert 'Личные кабинеты' in page.title_private_cabinets.get_text()

    assert page.title_history
    assert 'История действий' in page.title_history.get_text()


def test20_auth_unsuccess_incorrect_password(web_browser):
    """Проверка аутентификации пользователя по адресу email и паролю при вводе некорректных данных (верный
    логин, но неверный пароль). Негативный сценарий"""
    page = AuthPage(web_browser)
    page.auth_tab_email_button.click()
    page.username_field.send_keys(auth_email_valid)
    page.password_field.send_keys(auth_password_incorrect)
    page.auth_button.click()

    assert 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?execution' in page.get_current_url()

    assert page.error_login
    assert 'Неверный логин или пароль' in page.error_login.get_text() or 'Неверно введен текст с картинки' in page.error_login.get_text()


def test21_auth_unsuccess_incorrect_email(web_browser):
    """Проверка аутентификации пользователя по адресу email и паролю при вводе некорректных данных (верный
    пароль, но неверный логин). Негативный сценарий"""
    page = AuthPage(web_browser)
    page.auth_tab_email_button.click()
    page.username_field.send_keys(auth_email_incorrect)
    page.password_field.send_keys(auth_password_valid)
    page.auth_button.click()

    assert 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?execution' in page.get_current_url()

    assert page.error_login
    assert 'Неверный логин или пароль' in page.error_login.get_text() or 'Неверно введен текст с картинки' in page.error_login.get_text()


def test22_auth_tab_auto_change(web_browser):
    """Проверка автоматической смены типа авторизации (в поле "Телефон" ввод email)"""
    page = AuthPage(web_browser)
    page.auth_tab_phone_button.click()
    assert 'rt-tab--active' in page.auth_tab_phone_button.get_attribute('className')
    assert 'Телефон' in page.auth_tab_phone_button.get_text()

    page.username_field.send_keys(auth_email_valid)
    page.password_field.click()
    assert 'rt-tab--active' in page.auth_tab_email_button.get_attribute('className')
    assert 'Почта' in page.auth_tab_email_button.get_text()


def test23_auth_tab_auto_change(web_browser):
    """Проверка автоматической смены типа авторизации (в поле "Почта" ввод номера телефона)"""
    page = AuthPage(web_browser)
    page.auth_tab_email_button.click()
    assert 'rt-tab--active' in page.auth_tab_email_button.get_attribute('className')
    assert 'Почта' in page.auth_tab_email_button.get_text()

    page.username_field.send_keys(valid_phone)
    page.password_field.click()
    assert 'rt-tab--active' in page.auth_tab_phone_button.get_attribute('className')
    assert 'Телефон' in page.auth_tab_phone_button.get_text()


def test24_auth_tab_auto_change(web_browser):
    """Проверка перехода на страницу восстановления пароля при нажатии соответствующей кнопки на странице
    аутентификации"""
    page = AuthPage(web_browser)
    page.forget_password_button.click()

    assert page.title_reset_password
    assert 'Восстановление пароля' in page.title_reset_password.get_text()
    assert page.captcha_field
    assert page.reset_password_button


def test25_auth_privacy_policy_page(web_browser):
    """Проверка перехода на страницу с описанием политики конфиденциальности при нажатии соответствующей
    кнопки на странице аутентификации"""
    page = AuthPage(web_browser)
    page.privacy_policy_button.click()
    page.switch_to_new_window()
    time.sleep(3)
    page.screenshot('test25.jpg')

    assert 'private' in page.get_current_url()
    assert 'agreement' not in page.get_current_url()


def test26_auth_user_agreement_page(web_browser):
    """Проверка перехода на страницу с описанием пользовательского соглашения при нажатии соответствующей
    кнопки на странице аутентификации"""
    page = AuthPage(web_browser)
    page.user_agreement_button.click()
    page.switch_to_new_window()
    time.sleep(3)

    assert 'agreement' in page.get_current_url()
