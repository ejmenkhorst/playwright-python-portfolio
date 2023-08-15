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

- ```python -m pytest tests/e2e/ --browser webkit --headed```
- ```python -m pytest tests/e2e/ --browser firefox --headed```

#### API tests

With Playwright, we can also do API testing in the same framework.