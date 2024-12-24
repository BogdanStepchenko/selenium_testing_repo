# Selenium WebDriver Automation Testing

This repository contains automated tests for verifying the functionality of a web application using Selenium WebDriver. 
The tests cover various aspects of the website, including user sign-in, sale pages, eco-friendly product collections.

## 📋 Features

### General Features
- **Automated Web Interaction**: Tests for user interaction with the website, such as signing in, viewing product 
collections, and checking sales pages.
- **Element Verification**: Verifies that the elements on the page are present, correctly displayed, and 
contain the expected values.
- **Navigation Testing**: Ensures that navigation between pages works as expected, including URL changes and page titles

### Functional Blocks
- **Sign-In Page Tests**:
  - Verifies the ability to create an account with valid data.
  - Ensures appropriate error messages for invalid or incomplete data.
  - Validates successful account creation with correct confirmation messages.
  
- **Sale Page Tests**:
  - Verifies the correct display of sale cards on the sale page.
  - Checks for correct text and button values in the main sale card.
  - Validates navigation from the sale page to the specific women's sale page.

- **Eco-Friendly Product Collection Tests**:
  - Ensures the correct number of eco-friendly products are displayed.
  - Validates the ability to filter products by color and update the number of products shown.
  - Confirms the proper functionality of different product views (e.g., grid and list views).

- **Women Sale Page Tests**:
  - Ensures the page title is correctly displayed when navigating to the women’s sale page.
  - Validates the sale page URL and page title after navigating from the sale page.

## 📂 Project Structure

The project is organized into the following key directories:

### 1. **pages Folder**
Contains classes that represent different web pages. Each class includes methods for interacting with the 
page elements and performing actions.

- **base_page.py**: Contains base functionality for handling web elements, as locating and interacting with elements.
- **account_page.py**: Class for the account page, containing methods for verifying success messages.
- **collections_eco_friendly_page.py**: Class for eco-friendly products collection page, with filtering and pagination.
- **sale_page.py**: Class for the sale page, verifying that sale cards and their information are displayed correctly.
- **sign_in_page.py**: Class for the sign-in page, containing methods to input data and check for errors.
- **woman_sale_page.py**: Class for the women's sale page, used for validation after navigating from the sale page.

### 2. **tests Folder**
Contains automated test cases for verifying the functionality of the web pages. 
The tests use pytest and Selenium WebDriver.

- **test_sale_page.py**: Contains tests related to the sale page functionality.
- **test_collections_eco_friendly.py**: Tests for interacting with the eco-friendly collection page.
- **test_sign_in_page.py**: Tests for the sign-in page, including form validation and account creation.
- **conftest.py**: Contains pytest fixtures for setting up the driver and initializing pages.

### 3. **pages/locators Folder**
Contains locators for elements on each page. The locators are used in the page classes to interact with elements.

- **sale_page.py**: Contains locators for the sale page.
- **sign_in_page.py**: Contains locators for the sign-in page.
- **women_sale_page.py**: Contains locators for the women's sale page.

### 4. **pages/helper Folder**
Contains helper functions and randomizers for generating test data.

- **randomizer.py**: Generates random data such as names, emails, and passwords.
- **text_to_check.py**: Stores the text values that are used for validation in tests (e.g., error messages, titles).

## 🛠 Technologies Used
- **Python 3.12**: The programming language used for writing the automation tests.
- **pytest**: A testing framework used to write and execute the test cases.
- **Selenium WebDriver**: The tool used for browser automation to simulate user interactions with the website.
- **GitHub Actions**: For continuous integration and automatic test execution.

## 🚀 Running the Tests with Docker and CI/CD

### Running Tests with CI/CD

This project is integrated with GitHub Actions for Continuous Integration and Continuous Delivery (CI/CD). 
Whenever you push code to the `main` branch or create a pull request, the tests will automatically run in a Docker 
container using the Selenium WebDriver.

#### Workflow Steps:
1. The workflow is triggered on a `push` or `pull_request` event to the `main` branch.
2. The Docker image for Selenium WebDriver is built and used to run the tests.
3. The tests are executed based on the severity level chosen via the `workflow_dispatch` event 
(which allows for running specific types of tests like `fast_smoke`, `smoke`, or `full_test`).
4. After the tests are complete, an Allure report is generated.
5. The generated report is saved as an artifact and can be viewed via GitHub Pages.


### Running Tests Locally with Docker
To run the tests locally using Docker, follow these steps:

1. **Clone the Repository**:
   First, clone the repository to your local machine:
   ```bash
   git clone <repository-url>
   cd <repository-directory>

2. **Build the Docker Image**:
   In the root of the project directory, build the Docker image:
   ```bash
   docker build -t selenium-tests .
   
3**Run the Tests**:
   Once the image is built, you can run the tests using the following command:
   ```bash
    docker run selenium-tests
