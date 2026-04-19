import allure
from pages.login_page import LoginPage
from pages.password_settings_page import PasswordSettingsPage


@allure.feature("Настройки сложности пароля")
class TestPasswordSettings:

    @allure.story("Срок действия пароля")
    @allure.title("Срок = 5 дней - вход с валидным паролем успешен")
    def test_password_expiration_positive(self, password_settings_page: PasswordSettingsPage, login_page: LoginPage):

        with allure.step("Настроить срок действия пароля = 5 дней"):
            password_settings_page.set_expiration(5)
            password_settings_page.save()
            password_settings_page.should_be_saved()

        with allure.step("Попытка входа с валидным паролем"):
            login_page.fill_username("test_user")
            login_page.fill_password("ValidPass123!")
            login_page.submit()

        with allure.step("Проверка успешного входа"):
            login_page.should_login_success()

    # -------------------------

    @allure.story("Минимальная длина")
    @allure.title("Мин длина = 8 - пароль из 8 символов принимается")
    def test_min_length_positive(self, password_settings_page: PasswordSettingsPage, login_page: LoginPage):

        with allure.step("Установить минимальную длину = 8"):
            password_settings_page.set_min_length(8)
            password_settings_page.save()
            password_settings_page.should_be_saved()

        with allure.step("Вход с паролем длиной 8 символов"):
            login_page.fill_username("test_user")
            login_page.fill_password("Abc123!!")
            login_page.submit()

        with allure.step("Проверка успешного входа"):
            login_page.should_login_success()

    # -------------------------

    @allure.story("Минимальное количество цифр")
    @allure.title("Мин цифр = 2 - пароль с 2 цифрами принимается")
    def test_min_digits_positive(self, password_settings_page: PasswordSettingsPage, login_page: LoginPage):

        with allure.step("Установить минимум цифр = 2"):
            password_settings_page.set_min_digits(2)
            password_settings_page.save()

        with allure.step("Вход с валидным паролем (2 цифры)"):
            login_page.fill_username("test_user")
            login_page.fill_password("Abc12!!")
            login_page.submit()

        with allure.step("Проверка успешного входа"):
            login_page.should_login_success()

    # -------------------------

    @allure.story("Минимальное количество букв")
    @allure.title("Мин букв = 3 - пароль принимается")
    def test_min_letters_positive(self, password_settings_page: PasswordSettingsPage, login_page: LoginPage):

        with allure.step("Установить минимум букв = 3"):
            password_settings_page.set_min_letters(3)
            password_settings_page.save()

        with allure.step("Вход с паролем с достаточным числом букв"):
            login_page.fill_username("test_user")
            login_page.fill_password("abc123!!")
            login_page.submit()

        with allure.step("Проверка успешного входа"):
            login_page.should_login_success()

    # -------------------------

    @allure.story("Заглавные буквы")
    @allure.title("Мин заглавных = 2 - пароль принимается")
    def test_min_uppercase_positive(self, password_settings_page: PasswordSettingsPage, login_page: LoginPage):

        with allure.step("Установить минимум заглавных букв = 2"):
            password_settings_page.set_min_uppercase(2)
            password_settings_page.save()

        with allure.step("Вход с паролем с 2 заглавными буквами"):
            login_page.fill_username("test_user")
            login_page.fill_password("AbC123!!")
            login_page.submit()

        with allure.step("Проверка успешного входа"):
            login_page.should_login_success()

    # -------------------------

    @allure.story("Специальные символы")
    @allure.title("Мин спецсимволов = 2 - пароль принимается")
    def test_min_special_positive(self, password_settings_page: PasswordSettingsPage, login_page: LoginPage):

        with allure.step("Установить минимум спецсимволов = 2"):
            password_settings_page.set_min_special(2)
            password_settings_page.save()

        with allure.step("Вход с паролем с 2 спецсимволами"):
            login_page.fill_username("test_user")
            login_page.fill_password("Abc123!!")
            login_page.submit()

        with allure.step("Проверка успешного входа"):
            login_page.should_login_success()

    # -------------------------

    @allure.story("Повторяющиеся символы")
    @allure.title("Макс повторы = 2 - пароль без превышения принимается")
    def test_max_repeat_positive(self, password_settings_page: PasswordSettingsPage, login_page: LoginPage):

        with allure.step("Установить максимум повторов = 2"):
            password_settings_page.set_max_repeat(2)
            password_settings_page.save()

        with allure.step("Вход с допустимыми повторами"):
            login_page.fill_username("test_user")
            login_page.fill_password("Aabb11!!")
            login_page.submit()

        with allure.step("Проверка успешного входа"):
            login_page.should_login_success()

    # -------------------------

    @allure.story("Запрет последовательностей")
    @allure.title("Включен запрет - валидный пароль без последовательностей принимается")
    def test_no_sequences_positive(self, password_settings_page: PasswordSettingsPage, login_page: LoginPage):

        with allure.step("Включить запрет последовательностей"):
            password_settings_page.enable_no_sequences()
            password_settings_page.save()

        with allure.step("Вход с безопасным паролем"):
            login_page.fill_username("test_user")
            login_page.fill_password("XyZ9!kL2")
            login_page.submit()

        with allure.step("Проверка успешного входа"):
            login_page.should_login_success()

    # -------------------------

    @allure.story("Запрет года рождения")
    @allure.title("Включен запрет - пароль без года принимается")
    def test_no_birth_year_positive(self, password_settings_page: PasswordSettingsPage, login_page: LoginPage):

        with allure.step("Включить запрет года рождения"):
            password_settings_page.enable_no_birth_year()
            password_settings_page.save()

        with allure.step("Вход с паролем без года"):
            login_page.fill_username("test_user")
            login_page.fill_password("SafePass!23")
            login_page.submit()

        with allure.step("Проверка успешного входа"):
            login_page.should_login_success()

    # -------------------------

    @allure.story("Запрет клавиатурных комбинаций")
    @allure.title("Включен запрет - безопасный пароль принимается")
    def test_no_keyboard_sequences_positive(self, password_settings_page: PasswordSettingsPage, login_page: LoginPage):

        with allure.step("Включить запрет клавиатурных комбинаций"):
            password_settings_page.enable_no_keyboard()
            password_settings_page.save()

        with allure.step("Вход с валидным паролем"):
            login_page.fill_username("test_user")
            login_page.fill_password("Secure1!X")
            login_page.submit()

        with allure.step("Проверка успешного входа"):
            login_page.should_login_success()