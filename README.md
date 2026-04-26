# Stellar Burgers — UI End‑to‑End Test Automation

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/)
[![pytest](https://img.shields.io/badge/pytest-7.4+-orange.svg)](https://docs.pytest.org/)
[![Selenium](https://img.shields.io/badge/Selenium-4.15+-green.svg)](https://www.selenium.dev/)
[![Allure](https://img.shields.io/badge/Allure-2.13-purple.svg)](https://docs.qameta.io/allure/)
[![Page Object Model](https://img.shields.io/badge/Pattern-POM-blueviolet.svg)](https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/)
[![Cross Browser](https://img.shields.io/badge/Cross%20Browser-Chrome%20%7C%20Firefox-orange.svg)](https://www.selenium.dev/)

Automated end‑to‑end UI tests for [Stellar Burgers](https://stellarburgers.education-services.ru) – a burger constructor service.  
The project covers navigation, ingredient modal, order placement, and order feed counters.  
Tests run on **Google Chrome** and **Mozilla Firefox** with **Allure** reporting.

## Project Description

This project contains end‑to‑end UI tests built with **Selenium WebDriver**, **pytest**, and the **Page Object Model** pattern.  
It supports cross‑browser testing (Chrome, Firefox) and generates detailed **Allure** reports.

## Test Coverage

### Main Functionality
- Navigation by clicking "Constructor" button
- Navigation by clicking "Order Feed" button
- Click on an ingredient → ingredient details modal appears
- Close modal by clicking the cross icon
- Adding an ingredient to order → ingredient counter increases

### Order Feed
- After creating a new order, the "Total orders all time" counter increments
- After creating a new order, the "Total orders today" counter increments
- After placing an order, the order number appears in the "In progress" section

## Cross‑Browser Testing

All tests are designed to run on both **Google Chrome** and **Mozilla Firefox**.  
You can specify the browser via command line (see `conftest.py` fixture) or set as default.

## Project Structure

```
Stellar-Burgers-UI-E2E-Tests/
    ├── README.md
    ├── conftest.py
    ├── requirements.txt
    ├── pages/
    │   ├── base_page.py
    │   ├── ingredient_page.py
    │   ├── login_page.py
    │   ├── main_page.py
    │   └── order_feed_page.py
    └── tests/
        ├── test_ingredient.py
        ├── test_navigation.py
        ├── test_order_feed.py
        └── test_order_form.py
```

## Setup & Installation

### Requirements
- Python 3.12+
- Google Chrome / Mozilla Firefox (latest versions)
- Selenium
- pytest
- allure-pytest
- webdriver-manager (recommended)

### Installation

1. **Clone the repository**
```bash
   git clone https://github.com/nvbeznosova/Stellar-Burgers-UI-E2E-Tests.git
   cd Stellar-Burgers-UI-E2E-Tests
```

2. **Create and activate a virtual environment** 

```bash
   python -m venv .venv
   source .venv/bin/activate   # On macOS/Linux
   # .venv\Scripts\activate    # On Windows
```

3. **Install dependencies**
```bash
   pip install -r requirements.txt
```

## Running Tests 

1. **Run all tests in Chrome (default browser):**
```bash
   pytest tests/
```

2. **Run tests in Firefox**
```bash
   pytest tests/ --browser=firefox
```

3. **Run a specific test file**
```bash
   pytest tests/test_navigation.py
``` 

## Allure Reports

### To generate and view an Allure report locally 

1. **Run tests with Allure results**
```bash
   pytest --alluredir=allure-results tests/
 ```

2. **Generate and open the report**
```bash
   allure serve allure-results
```

In CI/CD (GitHub Actions) the report can be automatically published to GitHub Pages. 







## Дополнения
- Исправлены тесты для Firefox
- Добавлены тестовые классы и шаги Allure