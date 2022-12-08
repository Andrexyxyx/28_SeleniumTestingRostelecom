import os, time

from pages.base_page_rostelecom import WebPage
from pages.elements import WebElement, ManyWebElements

class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://b2c.passport.rt.ru/'

        super().__init__(web_driver, url)

    # Кнопка выбора авторизации по телефону на странице аутентификации
    auth_tab_phone_button = WebElement(id='t-btn-tab-phone')

    # Кнопка выбора авторизации по телефону на странице аутентификации
    auth_tab_email_button = WebElement(id='t-btn-tab-mail')

    # Поле "Электронная почта" на странице аутентификации
    username_field = WebElement(id='username')

    # Поле "Пароль" на странице аутентификации
    password_field = WebElement(id='password')

    # Кнопка "ВОЙТИ" на странице аутентификации
    auth_button = WebElement(id='kc-login')


    # Заголовок "Учетные данные" на странице личного кабинета"
    title_account_data = WebElement(xpath='//*[@id="app"]/main/div/div[2]/div[1]/h3[1]')

    # Заголовок "Безопасность" на странице личного кабинета"
    title_security = WebElement(xpath='//*[@id="app"]/main/div/div[2]/div[1]/h3[2]')

    # Заголовок "Личные кабинеты" на странице личного кабинета"
    title_private_cabinets = WebElement(xpath='//*[@id="app"]/main/div/div[2]/div[3]/h3')

    # Заголовок "История действий" на странице личного кабинета"
    title_history = WebElement(xpath='//*[@id="app"]/main/div/div[2]/div[2]/h3')

    # Сообщение при неудачной попытке аутентификации "Неверный логин или пароль"
    error_login = WebElement(id='form-error-message')

    # Кнопка "Забыл пароль" на странице аутентификации
    forget_password_button = WebElement(id='forgot_password')

    # Заголовок "Восстановление пароля" на странице восстановления пароля
    title_reset_password = WebElement(xpath='//*[@id="page-right"]/div/div/h1')

    # Поле "Капча" на странице восстановления пароля
    captcha_field = WebElement(id='captcha')

    # Кнопка "Продолжить" на странице восстановления пароля
    reset_password_button = WebElement(id='reset')

    # Кнопка "Политикой конфиденциальности" на странице аутентификации
    privacy_policy_button = WebElement(xpath='//*[@id="rt-footer-agreement-link"]/span[1]')

    # Кнопка "Пользовательским соглашением" на странице аутентификации
    user_agreement_button = WebElement(xpath='//*[@id="rt-footer-agreement-link"]/span[2]')