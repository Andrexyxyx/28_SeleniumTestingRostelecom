import os, time

from pages.base_page_rostelecom import WebPage
from pages.elements import WebElement, ManyWebElements

class RegPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://b2c.passport.rt.ru/'

        super().__init__(web_driver, url)

    # Кнопка перехода на страницу регистрации
    registration_button = WebElement(id='kc-register')

    # Поле "Имя" на странице регистрации
    firstname_field = WebElement(name='firstName')
    # Ошибка при введении некорректного значения в поле "Имя"
    error_firstname = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/span')

    # Поле "Фамилия" на странице регистрации
    lastname_field = WebElement(name='lastName')
    # Ошибка при введении некорректного значения в поле "Фамилия"
    error_lastname = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span')

    # Поле "Регион" на странице регистрации
    region_field = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[2]/div/div/input')

    # Поле "Email или мобильный телефон" на странице регистрации
    email_phone_field = WebElement(id='address')
    # Ошибка при введении некорректного значения в поле "Email или мобильный телефон"
    error_email_phone = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[3]/span')

    # Поле "Пароль" на странице регистрации
    password_field = WebElement(id='password')
    # Ошибка при введении некорректного значения в поле "Пароль" - "Длина пароля должна быть не менее 8 символов"
    error_password1 = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span')
    # Ошибка при введении некорректного значения в поле "Пароль" - "Пароль должен содержать хотя бы одну заглавную букву"
    error_password2 = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span')
    # Ошибка при введении некорректного значения в поле "Пароль" - "Пароль должен содержать только латинские буквы"
    error_password3 = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span')

 # Поле "Подтверждение пароля" на странице регистрации
    confirm_password_field = WebElement(id='password-confirm')
    # Ошибка при введении несовпадающих паролей в поля "Пароль" и "Подтверждение пароля" - "Пароли не совпадают"
    error_confirm_password = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/span')

    # Кнопка "ЗАРЕГИСТРИРОВАТЬСЯ" на странице регистрации
    registration_submit_button = WebElement(name='register')


