# RideCellAssignment

Technology Stack:

1. Python 3.9
2. Selenium Library 3.141.0
3. requests Library 2.25.1
4. pytest 6.2.2
5. pytest-html 3.1.1

Framework Structure:

Framework -

  -- Configuration_files
  
  -- Logs
  
  -- POM
  
  -- results
  
  -- tests
  
  -- utilities
  

How to Run This Framework ?

1. git clone this repository
2. cd RideCellAssignment/venv
3. pipenv install
4. Go to cd venv then pipenv install
5. Go to cd venv/Framework
6. Then run pytest -v --html=results/report.html tests/test_Django.py --browser chrome
