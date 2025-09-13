# API тесты для Кинопоиск
import pytest
import allure
import requests
from config import settings

HEADERS = {
    "X-API-KEY": settings.API_KEY
}

@allure.step('Поиск по полному названию фильма')
def test_search_full_title():
    params = {"page": 1, "limit": 10, "query": "Интерстеллар"}
    r = requests.get(settings.API_URL, headers=HEADERS, params=params)
    assert r.status_code == 200
    assert any("Интерстеллар" in m.get("name", "") for m in r.json().get("docs", []))

@allure.step('Поиск по частичному названию')
def test_search_partial_title():
    params = {"page": 1, "limit": 10, "query": "Интер"}
    r = requests.get(settings.API_URL, headers=HEADERS, params=params)
    assert r.status_code == 200
    assert any("Интер" in m.get("name", "") for m in r.json().get("docs", []))

@allure.step('Поиск по английскому названию')
def test_search_english_title():
    params = {"page": 1, "limit": 10, "query": "interstellar"}
    r = requests.get(settings.API_URL, headers=HEADERS, params=params)
    assert r.status_code == 200
    assert any("Interstellar" in m.get("alternativeName", "") for m in r.json().get("docs", []))

@allure.step('Поиск несуществующего фильма')
def test_search_nonexistent():
    params = {"page": 1, "limit": 10, "query": "gFHu86UIu7"}
    r = requests.get(settings.API_URL, headers=HEADERS, params=params)
    assert r.status_code == 200
    assert len(r.json().get("docs", [])) == 0

@allure.step('Пустой параметр поиска')
def test_search_empty():
    params = {"query": ""}
    r = requests.get(settings.API_URL, headers=HEADERS, params=params)
    assert r.status_code == 200
    # API возвращает не пустой список, поэтому просто проверяем статус

@allure.step('Слишком длинный запрос')
def test_search_long_query():
    long_query = "Идейные соображения высшего порядка, а также укрепление и развитие структуры в значительной степени обусловливает создание системы обучения кадров, соответствует насущным потребностям. " * 5
    params = {"page": 1, "limit": 10, "query": long_query}
    r = requests.get(settings.API_URL, headers=HEADERS, params=params)
    assert r.status_code == 200

@allure.step('Число вместо названия')
def test_search_number():
    params = {"page": 1, "limit": 10, "query": "152688645"}
    r = requests.get(settings.API_URL, headers=HEADERS, params=params)
    assert r.status_code == 200
