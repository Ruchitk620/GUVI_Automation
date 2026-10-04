# GUVI EdTech Platform – Selenium Automation

## Project Overview

This project contains an automated functional testing suite for the **GUVI EdTech Platform** web application using Selenium WebDriver with Python and pytest.

The automation focuses on validating important user-facing flows on the GUVI website, including homepage access, navigation, login, invalid login handling, sign-up navigation, main menu visibility, the Dobby/Chat Assistant, and logout.

**Application Under Test:** GUVI  
**Application URL:** https://www.guvi.in/

---

## Objectives

The main objectives of this automation project are to:

- Validate key GUVI homepage elements and navigation.
- Verify login and invalid-login behavior.
- Verify sign-up button visibility and navigation.
- Verify main menu items are visible and accessible.
- Verify the GUVI Dobby/Chat Assistant is present.
- Verify that a valid authenticated user can log in and log out.
- Generate an HTML execution report using pytest-html.

---

## Technology Stack

| Technology / Tool | Usage |
|---|---|
| Python | Automation programming language |
| Selenium WebDriver | Browser automation |
| pytest | Test framework and test execution |
| pytest-html | HTML test reporting |
| Chrome / ChromeDriver | Browser execution |
| Page Object Model (POM) | Test design and maintainability |
| PowerShell | Environment-variable configuration and execution |
| Git / GitHub | Source-code management |

---

## Project Structure

```text
GUVI_Automation/
│
├── pages/
│   ├── __init__.py
│   ├── dashboard_page.py
│   ├── home_page.py
│   ├── login_page.py
│   └── signup_page.py
│
├── tests/
│   ├── __init__.py
│   ├── test_dobby.py
│   ├── test_home_url.py
│   ├── test_invalid_login.py
│   ├── test_login_button.py
│   ├── test_logout.py
│   ├── test_menu_items.py
│   ├── test_signup_button.py
│   ├── test_signup_navigation.py
│   ├── test_title.py
│   └── test_valid_login.py
│
├── utils/
│   └── __init__.py
│
├── conftest.py
├── requirements.txt
├── report.html
├── .gitignore
└── README.md
```

---

## Test Coverage

### 1. Homepage

- Verify GUVI homepage URL.
- Verify homepage title.
- Verify Login button visibility, clickability and navigation.
- Verify Sign-Up button visibility, clickability and navigation.
- Verify main menu items:
  - Courses
  - Practice
  - LIVE Classes

### 2. Authentication

- Verify valid login with configured test credentials.
- Verify invalid login displays:
  `Incorrect Email or Password`
- Verify logout after successful authentication.

### 3. GUVI Dobby / Chat Assistant

- Verify the GUVI Dobby/Chat Assistant is present after the page is loaded and scrolled.

### 4. Sign-Up Navigation

- Verify the Sign-Up button navigates to the GUVI registration page.
- Verify the resulting URL.

---

## Test Cases

| Test Case | Description |
|---|---|
| test_home_url | Verify GUVI homepage URL |
| test_title | Verify homepage title |
| test_login_button | Verify Login button and navigation |
| test_invalid_login | Verify invalid credentials handling |
| test_valid_login | Verify successful login |
| test_logout | Verify user logout |
| test_signup_button | Verify Sign-Up button and navigation |
| test_signup_navigation | Verify Sign-Up URL |
| test_menu_items | Verify main menu items |
| test_dobby | Verify Dobby/Chat Assistant presence |

---

## Page Object Model

The framework follows the **Page Object Model (POM)** approach.

### HomePage
Contains locators and reusable methods for:

- Homepage navigation
- Login button
- Sign-Up button
- Main menu items
- Dobby/Chat Assistant
- Cookie-banner handling

### LoginPage
Contains reusable methods for:

- Opening the sign-in page
- Entering email
- Entering password
- Clicking Login
- Validating login-page state
- Validating invalid-login error messages

### DashboardPage
Contains methods for:

- Handling the authenticated header
- Opening the account menu
- Logging out

### SignupPage
Contains sign-up-page related page-object functionality.

---

## WebDriver Fixture

The Selenium WebDriver is created and managed through `conftest.py`.

The fixture:

1. Creates a Chrome WebDriver.
2. Configures browser preferences.
3. Maximizes the browser window.
4. Provides the driver to each test.
5. Quits the browser after the test completes.

This keeps browser setup and teardown centralized.

---

## Test Credentials Configuration

The valid-login and logout tests require a real GUVI test account.

**Do not hard-code or commit the actual email address or password to GitHub.**

For Windows PowerShell, configure the credentials in the current terminal session:

```powershell
$env:GUVI_VALID_EMAIL="your_guvi_email"
$env:GUVI_VALID_PASSWORD="your_guvi_password"
```

You can verify that the variables are available with:

```powershell
$env:GUVI_VALID_EMAIL
$env:GUVI_VALID_PASSWORD
```

Then run the tests.

These environment variables are used by:

- `tests/test_valid_login.py`
- `tests/test_logout.py`

---

## Installation

Create and activate a Python virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the required packages:

```powershell
python -m pip install -r requirements.txt
```

---

## Running the Tests

Run the complete test suite:

```powershell
python -m pytest -v -s
```

Run selected tests:

```powershell
python -m pytest -v -s tests/test_valid_login.py tests/test_logout.py
```

Generate the HTML report:

```powershell
python -m pytest -v -s --html=report.html --self-contained-html
```

---

## Test Execution Report

A pytest-html report is included as:

`report.html`

The latest committed report contains the execution results from the configured environment.

For the successful credential-configured execution, the report records:

- **Total tests:** 10
- **Passed:** 10
- **Failed:** 0
- **Skipped:** 0
- **Execution time:** 00:01:23

The report also contains the pytest environment information and individual test results.

> Note: The two authentication-dependent tests require `GUVI_VALID_EMAIL` and `GUVI_VALID_PASSWORD` to be configured. Running the suite without these variables will cause those tests to fail during test-data validation before the authentication steps execute.

---

## Coding Practices

The project uses:

- Page Object Model for reusable page interactions.
- Explicit waits with Selenium `WebDriverWait`.
- Expected Conditions for synchronization.
- Environment variables for sensitive test credentials.
- Reusable page-level methods instead of duplicating Selenium interactions.
- pytest for structured test execution.
- pytest-html for execution reporting.

---

## GitHub

Repository:

https://github.com/Ruchitk620/GUVI_Automation

The repository is intended to contain the source code, configuration files, README, and HTML execution report while excluding local environment/cache files through `.gitignore`.

---

## Important Notes

- The GUVI website is a live web application and UI behavior, locators, redirects, cookies, or dynamically loaded elements can change over time.
- The valid-login and logout scenarios depend on a working GUVI test account.
- Never upload real credentials, passwords, tokens, or other secrets to the repository.
- Run the tests in a stable internet-connected environment with Chrome available.

---

## Author

**Ruchit Kumar**
