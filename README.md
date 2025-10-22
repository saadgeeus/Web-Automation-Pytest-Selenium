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
├── conftest.py
├── pytest.ini
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
└── Jenkinsfile
└── run_tests.py
```


## Setup
1. Create a Python virtual environment:


```bash
python -m venv .venv
source .venv/bin/activate # Linux / macOS
.venv\Scripts\activate # Windows
```
2. Install requirements:
```bash
pip install -r requirements.txt
```
3. Run tests:
```bash
# run all tests and generate html report
pytest -q --html=reports/test_report.html


# run a specific test
pytest tests/test_login.py -q
```
4. Open ```reports/test_report.html``` to view results.
---
## Test credentials (SauceDemo)
- username: ```standard_user```
- password: ```secret_sauce```

## Notes
- Chrome is required on the machine. ```webdriver-manager``` will download the appropriate chromedriver.
- Adjust timeouts and waits in ```utils/driver_setup.py``` if needed.

---
## How To Use:
1. Clone This Repo From This Link: [Web Automation Pytest Selenium](https://github.com/saadgeeus/Web-Automation-Pytest-Selenium)
2. Create and activate a virtual environment and install requirements.txt.
3. Run ```pytest -q --html=reports/test_report.html``` or ```python run_tests.py```.
