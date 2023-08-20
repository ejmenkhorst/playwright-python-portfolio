# Playwright Python

This repo is my playground for applying Python with Playwright.

## Project setup

Please install all required packages by running ``` pip install -r requirements.txt```

### Page Object Model

All the page object models / components are stored in the **models** folder.

### Tests

To execute the tests we make use of the PytTest testrunner.  
The command to execute the tests is: ```pytest```

#### E2E tests

The beauty of the Playwright framework is that it manages automatically all the latest browser versions locally - you
never have to align these manually on your local machine.

We can run different browser engines with Playwright:

- Chromium (by default - and always headless)
- Firefox
- Webkit

To run on of these explicitly you can add it to the CLI with the --browser flag.

- ```python -m pytest tests/e2e/ --browser chromium --headed --base-url https://automationintesting.online```
- ```python -m pytest tests/e2e/ --browser webkit --headed --base-url https://automationintesting.online```
- ```python -m pytest tests/e2e/ --browser firefox --headed --base-url https://automationintesting.online```

#### API tests with Playwright

With Playwright, we can also do API testing in the same framework.
For this demo purpose I used
an [Vehicle Fleet Management API](https://car-fleet-management.herokuapp.com/swagger-ui.html) with simple CRUD
operations.

To do a proper setup and teardown proces I implemented it with the help of fixtures which you can find
in [conftest.py](tests/conftest.py)

To run on of these explicitly you can add it to the CLI with the following command:

- ```python -m pytest tests/api/ --base-url https://car-fleet-management.herokuapp.com```
