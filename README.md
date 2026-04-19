## Установка зависимостей

- pip install -r requirements.txt

## Установка браузеров

- playwright install

## Как запускать?

Запуск всех тестовых с подробным выводом и открытием браузера
- pytest -v --headed 

Запуск по ключевому слову
- pytest -k "ключевое слово"

## Как посмотреть результаты allure отчета?

В pytest.ini добавлен --alluredir=allure-results и после прогона будет создана папка allure-result

Открыть отчет в браузере
- allure serve allure-results