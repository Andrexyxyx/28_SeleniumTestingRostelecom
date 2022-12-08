# 28_SeleniumTestingRostelecom

Автоматизированное тестирование веб-интерфейсов сайта Ростелеком https://b2c.passport.rt.ru/ с помощью Selenium.

В папке pages находятся файлы, описывающие шаблоны страниц и непосредственно страницы сайта https://b2c.passport.rt.ru/.

В файле pages/base_page_rostelecom.py содержится реализацию шаблона PageObject для Python.

В файле pages/elements.py содержится вспомогательный класс для определения веб-элементов на веб-страницах.

В файле pages/config_rostelecom.py содержится информация о валидных и невалидных данных, необходимых для регистрации и аутентификации пользователя.

В файле pages/reg_page_rostelecom.py содержится класс страницы регистрации на сайте Ростелеком https://b2c.passport.rt.ru/.

В файле pages/confirm_reg_page_rostelecom.py содержится класс страницы подтверждения регистрации на сайте Ростелеком https://b2c.passport.rt.ru/.

В файле pages/auth_page_rostelecom.py содержится класс страницы аутентификации на сайте Ростелеком https://b2c.passport.rt.ru/.

В файле tests/test_reg_auth_page_rostelecom.py располагается набор тестов для веб-интерфейса сайта Ростелеком https://b2c.passport.rt.ru/.

В файле requirements.txt находится список требуемых к установке библиотек.


ИНСТРУКЦИЯ ПО ЗАПУСКУ:
1. Скачать драйвер для браузера Google Chrome - https://chromedriver.chromium.org/downloads
2. Установить все требуемые библиотеки из файла requirements.txt с помощью команды:
    pip install -r requirements.txt
3. Запустить разработанные тесты с помощью команды:
    python -m pytest -v --driver Chrome --driver-path C:/Documents/chromedriver.exe tests/test_reg_auth_page_rostelecom.py
    (где C:/Documents - папка с расположением драйвера Chrome)
