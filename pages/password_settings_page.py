import allure


class PasswordSettingsPage:

    def __init__(self, page):
        self.page = page

        # Поля
        self.expiration_input = page.get_by_role("spinbutton", name="Срок годности пароля")
        self.min_length_input = page.get_by_role("spinbutton", name="Минимальная длина")
        self.min_digits_input = page.get_by_role("spinbutton", name="Минимальное число цифр")
        self.min_letters_input = page.get_by_role("spinbutton", name="Минимальное число букв")
        self.min_uppercase_input = page.get_by_role("spinbutton", name="Минимальное число заглавных букв")
        self.min_special_input = page.get_by_role("spinbutton", name="Минимальное число специальных символов")
        self.max_repeat_input = page.get_by_role("spinbutton", name="Максимальная длина повторяющихся символов")

        # Переключатели
        self.no_sequences_checkbox = page.get_by_role("checkbox", name="Запрет алфавитных комбинаций")
        self.no_birth_year_checkbox = page.get_by_role("checkbox", name="Запрет года рождения")
        self.no_keyboard_checkbox = page.get_by_role("checkbox", name="Запрет клавиатурных комбинаций")

        # Кнопки / сообщения
        self.save_button = page.get_by_role("button", name="Сохранить")
        self.success_message = page.get_by_text("Настройки успешно сохранены")

    @allure.step("Открыть страницу настроек")
    def open(self):
        self.page.goto("https://example.com/password-settings")

    @allure.step("Установить срок действия: {days}")
    def set_expiration(self, days: int):
        self.expiration_input.fill(str(days))

    @allure.step("Установить минимальную длину: {value}")
    def set_min_length(self, value: int):
        self.min_length_input.fill(str(value))

    @allure.step("Установить мин. цифры: {value}")
    def set_min_digits(self, value: int):
        self.min_digits_input.fill(str(value))

    @allure.step("Установить мин. буквы: {value}")
    def set_min_letters(self, value: int):
        self.min_letters_input.fill(str(value))

    @allure.step("Установить мин. заглавные: {value}")
    def set_min_uppercase(self, value: int):
        self.min_uppercase_input.fill(str(value))

    @allure.step("Установить мин. спецсимволы: {value}")
    def set_min_special(self, value: int):
        self.min_special_input.fill(str(value))

    @allure.step("Установить макс. повторы: {value}")
    def set_max_repeat(self, value: int):
        self.max_repeat_input.fill(str(value))

    @allure.step("Включить запрет последовательностей")
    def enable_no_sequences(self):
        self.no_sequences_checkbox.check()

    @allure.step("Включить запрет года рождения")
    def enable_no_birth_year(self):
        self.no_birth_year_checkbox.check()

    @allure.step("Включить запрет клавиатурных комбинаций")
    def enable_no_keyboard(self):
        self.no_keyboard_checkbox.check()

    @allure.step("Сохранить настройки")
    def save(self):
        self.save_button.click()

    @allure.step("Проверить успех")
    def should_be_saved(self):
        assert self.success_message.is_visible()