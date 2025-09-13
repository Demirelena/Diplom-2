# UI тесты для Кинопоиск
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from config import settings, test_data

@allure.step('Открываем главную страницу')
def open_main_page(driver):
    driver.get(settings.BASE_URL)

@allure.step('Проверяем наличие кнопки Войти')
def check_login_button(driver):
    assert driver.find_element(By.CLASS_NAME, 'styles_loginButton__6_QNl').is_displayed()

@allure.step('Нажимаем на кнопку Войти')
def click_login_button(driver):
    driver.find_element(By.CLASS_NAME, 'styles_loginButton__6_QNl').click()

@allure.step('Проверяем наличие поля логина')
def check_login_field(driver):
    assert driver.find_element(By.ID, 'passp-field-login').is_displayed()

@allure.step('Вводим логин')
def input_login(driver):
    driver.find_element(By.ID, 'passp-field-login').send_keys(test_data.LOGIN)

@allure.step('Проверяем наличие кнопки Войти на форме')
def check_login_form_button(driver):
    assert driver.find_element(By.XPATH, "//span[text()='Войти']").is_displayed()

@allure.step('Нажимаем кнопку Войти на форме')
def click_login_form_button(driver):
    # Кликаем по кнопке, а не по span, чтобы избежать перехвата клика
    driver.find_element(By.ID, "passp:sign-in").click()

@allure.step('Вводим пароль')
def input_password(driver):
    driver.find_element(By.ID, 'passp-field-passwd').send_keys(test_data.PASSWORD)

@allure.step('Нажимаем кнопку Продолжить')
def click_continue_button(driver):
    # Кликаем по родительской кнопке, чтобы избежать перехвата клика
    driver.find_element(By.XPATH, "//button[@id='passp:sign-in' or @data-t='button:action:passp:sign-in' or .//span[text()='Продолжить']]").click()

@allure.step('Проверяем наличие поля поиска')
def check_search_field(driver):
    assert driver.find_element(By.NAME, 'kp_query').is_displayed()

@allure.step('Вводим название фильма и ищем')
def search_movie(driver):
    search_input = driver.find_element(By.NAME, 'kp_query')
    search_input.send_keys(test_data.SEARCH_MOVIE)
    search_input.send_keys(Keys.ENTER)

@allure.step('Проверяем наличие фильма Интерстеллар')
def check_movie_present(driver):
    assert driver.find_element(By.XPATH, "//a[contains(text(), 'Интерстеллар')]").is_displayed()

@pytest.fixture(scope='function')
def driver():
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')  # Отключено для ручного прохождения капчи
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(15)  # Ждем появления элементов и даем время пройти капчу вручную
    yield driver
    driver.quit()

def test_full_login_and_search(driver):
    open_main_page(driver)
    check_login_button(driver)
    click_login_button(driver)
    check_login_field(driver)
    input_login(driver)
    check_login_form_button(driver)
    click_login_form_button(driver)
    input_password(driver)
    click_continue_button(driver)
    check_search_field(driver)
    search_movie(driver)
    check_movie_present(driver)
