# UI тесты для Кинопоиск
import pytest
import allure

# Новые UI тесты для Кинопоиск
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from config import settings


SEARCH_TEXT = "интер"

@pytest.fixture(scope='session')
def driver():
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')  # Для ручной проверки
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(15)
    yield driver
    driver.quit()

@allure.step('Открываем главную страницу')
def open_main_page(driver):
    driver.get(settings.BASE_URL)

@allure.step('Проверяем наличие поля поиска')
def test_search_field_present(driver):
    open_main_page(driver)
    search_input = driver.find_element(By.NAME, "kp_query")
    assert search_input.is_displayed()
    search_input.send_keys(SEARCH_TEXT)

@allure.step('Проверяем наличие кнопки поиска и нажимаем')
def test_search_button_click(driver):
    open_main_page(driver)
    search_input = driver.find_element(By.NAME, "kp_query")
    search_input.send_keys(SEARCH_TEXT)
    search_btn = driver.find_element(By.CSS_SELECTOR, "button.styles_submit__KkHEO")
    assert search_btn.is_displayed()
    search_btn.click()

@allure.step('Проверяем наличие фильма Интерстеллар в выдаче')
def test_movie_present_in_results(driver):
    open_main_page(driver)
    search_input = driver.find_element(By.NAME, "kp_query")
    search_input.send_keys(SEARCH_TEXT)
    driver.find_element(By.CSS_SELECTOR, "button.styles_submit__KkHEO").click()
    movie_link = driver.find_element(By.XPATH, "//a[contains(text(), 'Интерстеллар')]")
    assert movie_link.is_displayed()

@allure.step('Проверяем, что страница фильма открывается по картинке')
def test_movie_page_opens(driver):
    open_main_page(driver)
    search_input = driver.find_element(By.NAME, "kp_query")
    search_input.send_keys(SEARCH_TEXT)
    driver.find_element(By.CSS_SELECTOR, "button.styles_submit__KkHEO").click()
    img = driver.find_element(By.XPATH, "//img[@alt='Интерстеллар']")
    assert img.is_displayed()
    img.click()
    # Проверяем, что открылась страница фильма по наличию заголовка
    assert "Интерстеллар" in driver.page_source

@allure.step('Проверяем, что рейтинг фильма больше 8')
def test_movie_rating(driver):
    open_main_page(driver)
    search_input = driver.find_element(By.NAME, "kp_query")
    search_input.send_keys(SEARCH_TEXT)
    driver.find_element(By.CSS_SELECTOR, "button.styles_submit__KkHEO").click()
    driver.find_element(By.XPATH, "//a[contains(text(), 'Интерстеллар')]").click()
    rating = driver.find_element(By.CSS_SELECTOR, "span.styles_ratingKpTop__8p7mM")
    assert rating.is_displayed()
    rating_value = float(rating.text.replace(',', '.'))
    assert rating_value > 8
    
