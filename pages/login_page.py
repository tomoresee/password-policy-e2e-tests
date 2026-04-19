import allure


class LoginPage:

    def __init__(self, page):
        self.page = page

        self.username_input = page.get_by_role("textbox", name="Логин")
        self.password_input = page.get_by_role("textbox", name="Пароль")
        self.login_button = page.get_by_role("button", name="Войти")

        self.error_message = page.get_by_text("Пароль не соответствует требованиям")
        self.success_login = page.get_by_text("Добро пожаловать")

    @allure.step("Открыть страницу логина")
    def open(self):
        self.page.goto("https://example.com/login")

    @allure.step("Ввести логин: {username}")
    def fill_username(self, username):
        self.username_input.fill(username)

    @allure.step("Ввести пароль")
    def fill_password(self, password):
        self.password_input.fill(password)

    @allure.step("Нажать Войти")
    def submit(self):
        self.login_button.click()

    @allure.step("Проверить успешный вход")
    def should_login_success(self):
        assert self.success_login.is_visible()

    @allure.step("Проверить ошибку пароля")
    def should_see_error(self):
        assert self.error_message.is_visible()