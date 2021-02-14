# RideCellAssignment

This is a Test Automation project that compares names and description of all repositories in django project from UI with respect to API. This framework is designed on following environment:

1. Mac OS Big Sur
2. PyCharm IDE : Community Version 2020.2

## Technology Stack:

1. Python 3.9
2. Selenium Library 3.141.0
3. requests Library 2.25.1
4. pytest 6.2.2
5. pytest-html 3.1.1

## Framework Structure:

Framework -

  -- Configuration_files
  
  -- Logs
  
  -- POM
  
  -- results
  
  -- tests
  
  -- utilities
  

## System Requirements:

Please install Python 3.9 version if not installed.

https://www.python.org/downloads/release/python-390/

## How to Run This Framework ?

1. git clone this repository
2. cd RideCellAssignment/venv
3. pipenv install
4. Go to cd venv then pipenv install
5. Then please download Chromedriver and Geckodriver binaries as per OS and place it in bin folder of the venv. Currently this framework supports two browser chrome and firefox which you can mention in the argument option in step 7.
6. Go to cd venv/Framework
7. Then run pytest -v --html=results/report.html tests/test_Django.py --browser chrome
