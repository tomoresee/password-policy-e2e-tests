1. Установить зависимостей

pip install -r requirements.txt

2. Установить браузеры

playwright install

3. Как запускать?

Запуск всех тестовых с подробным выводом и открытием браузера
- pytest -v --headed 

Запуск по ключевому слову
- pytest -k "ключевое слово"

4. Как посмотреть результаты allure отчета?

В pytest.ini добавлен --alluredir=allure-results и после прогона будет создана папка allure-result

Открыть отчет в браузере
- allure serve allure-results