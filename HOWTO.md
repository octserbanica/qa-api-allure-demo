
# HOW TO RUN – Allure Reporting Demo

## 1 Install dependencies

pip install -r requirements.txt

## 2 Install Allure

Mac:
brew install allure

Windows:
scoop install allure

or

npm install -g allure-commandline

## 3 Run tests

pytest --alluredir=allure-results

## 4 Generate report

allure serve allure-results

A browser window will open with the test report dashboard.
