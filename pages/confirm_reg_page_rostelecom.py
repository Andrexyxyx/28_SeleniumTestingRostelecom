import os, time

from pages.base_page_rostelecom import WebPage
from pages.elements import WebElement, ManyWebElements

class ConfirmRegPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://b2c.passport.rt.ru/'

        super().__init__(web_driver, url)

    # Заголовок "Подтверждение email" на странице подтверждения email
    confirm_email_title = WebElement(xpath='//*[@id="page-right"]/div/div/h1')

    # Кнопка "Изменить email" на странице подтверждения email
    change_email_button = WebElement(name='otp_back_phone')

