# Автоматизация UI и API тестов для Кинопоиск

## Описание
Автоматизированы UI и API тесты для сайта [Кинопоиск](https://www.kinopoisk.ru/). В проекте реализованы:
- UI-тесты авторизации и поиска фильма
- API-тесты поиска фильма
- Запуск тестов в разных режимах
- Документированный код с allure
- Все настройки и тестовые данные вынесены в отдельные файлы

## Структура проекта
- `tests/test_ui.py` — UI тесты (Selenium)
- `tests/test_api.py` — API тесты (requests)
- `config/settings.py` — настройки окружения
- `config/test_data.py` — тестовые данные
- `requirements.txt` — зависимости
- `run_tests.py` — запуск тестов в разных режимах

## Установка зависимостей
Установите Python 3.10+ и выполните:
```
pip install -r requirements.txt
```

## Запуск тестов
- Только UI: `python run_tests.py ui`
- Только API: `python run_tests.py api`
- Все тесты: `python run_tests.py`

## Особенности UI-тестов
- При авторизации на сайте появляется капча. Пройдите её вручную, тесты ожидают до 15 секунд.
- Для корректной работы UI-тестов браузер должен быть открыт (режим headless отключён).

## Линтер
Проверка PEP8:
```
flake8 tests/ config/
```

## Allure отчёты
1. Запустите тесты с генерацией отчёта:
	```
	pytest --alluredir=allure-results
	```
2. Сгенерируйте HTML-отчёт:
	```
	allure generate allure-results -o allure-report --clean
	```
3. Откройте отчёт в браузере:
	```
	allure open allure-report
	```
Если команда `allure` не найдена, скачайте Allure CLI: https://docs.qameta.io/allure/

## Финальный проект
Ссылка: [https://www.kinopoisk.ru/](https://www.kinopoisk.ru/)
# Автоматизация UI и API тестов для Кинопоиск

## Описание
Автоматизированы UI и API тесты для сайта [Кинопоиск](https://www.kinopoisk.ru/). В проекте реализованы:
- UI-тесты авторизации и поиска фильма
- API-тесты поиска фильма
- Запуск тестов в разных режимах
- Документированный код с allure
- Все настройки и тестовые данные вынесены в отдельные файлы

## Структура проекта
- `tests/test_ui.py` — UI тесты (Selenium)
- `tests/test_api.py` — API тесты (requests)
- `config/settings.py` — настройки окружения
- `config/test_data.py` — тестовые данные
- `requirements.txt` — зависимости

## Запуск тестов
- Только UI: `pytest tests/test_ui.py`
- Только API: `pytest tests/test_api.py`
- Все тесты: `pytest tests/`

## Линтер
Проверка PEP8: `flake8 tests/ config/`

## Финальный проект
Ссылка: [https://www.kinopoisk.ru/](https://www.kinopoisk.ru/)
