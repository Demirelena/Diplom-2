# UI & API Test Automation — Kinopoisk

Automated test suite for [Kinopoisk](https://www.kinopoisk.ru/) — Russia's largest movie database and streaming platform.

## About the Project

This is a graduation project completed as part of the **QA Automation Engineer** program at [Skypro](https://skypro.ru/). It demonstrates practical skills in UI and API test automation using Python.

## What Is Tested

### UI Tests (Selenium)
- User authentication (login flow)
- - Movie search functionality
 
  - ### API Tests (requests)
  - - Movie search API endpoint
    - - Response validation
     
      - ## Tech Stack
     
      - | Tool | Purpose |
      - |------|---------|
      - | Python 3.10+ | Programming language |
      - | Pytest | Test framework |
      - | Selenium WebDriver | UI automation |
      - | requests | API testing |
      - | Allure | Test reporting |
      - | flake8 | Code linting (PEP8) |
     
      - ## Project Structure
     
      - ```
        Diplom-2/
        ├── tests/
        │   ├── test_ui.py       # UI tests (Selenium)
        │   └── test_api.py      # API tests (requests)
        ├── config/
        │   ├── settings.py      # Environment settings
        │   └── test_data.py     # Test data
        ├── requirements.txt     # Dependencies
        ├── conftest.py          # Pytest fixtures
        └── run_tests.py         # Test runner (multiple modes)
        ```

		## Installation

```bash
# Clone the repository
git clone https://github.com/Demirelena/Diplom-2.git
cd Diplom-2

# Install dependencies
pip install -r requirements.txt
```

## Running Tests

```bash
# Run all tests
python run_tests.py

# Run UI tests only
python run_tests.py ui

# Run API tests only
python run_tests.py api
```

> **Note:** UI tests require manual CAPTCHA solving on login. The browser runs in non-headless mode and waits up to 15 seconds for manual input.
>
> ## Allure Reports
>
> ```bash
> # Run tests and generate results
> pytest --alluredir=allure-results
>
> # Generate HTML report
> allure generate allure-results -o allure-report --clean
>
> # Open report in browser
> allure open allure-report
> ```
>
> ## Code Quality
>
> ```bash
> # Check PEP8 compliance
> flake8 tests/ config/
> ```
>
> ## Author
>
> **Elena Demir** — QA Engineer (Manual & Automation)
> - GitHub: [github.com/Demirelena](https://github.com/Demirelena)
> - - LinkedIn: [linkedin.com/in/elena-demir-74110a213](https://linkedin.com/in/elena-demir-74110a213)
