# Web Automation Testing with Python & Selenium


This repo implements an end-to-end automation framework that tests sample e-commerce flows on `https://www.saucedemo.com`.


Features:
- Page Object Model (POM) structure
- pytest test runner
- webdriver-manager integration (auto-download ChromeDriver)
- HTML reports via `pytest --html` or `pytest-html`
- Example tests: login, search/add-to-cart, checkout
----
## Repository structure
```bash
web-automation-selenium/
│
├── README.md
├── requirements.txt
├── tests/
│   ├── test_login.py
│   ├── test_checkout.py
│   └── test_search.py
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── product_page.py
│   └── checkout_page.py
│
├── utils/
│   ├── driver_setup.py
│   └── config.py
│
├── reports/
│   └── test_report.html
│
└── run_tests.py
```


## Setup
1. Create a Python virtual environment:


```bash
python -m venv .venv
source .venv/bin/activate # Linux / macOS
.venv\Scripts\activate # Windows
```
