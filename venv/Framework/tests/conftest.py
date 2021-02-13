import pytest
import os
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    driver = ""
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    return driver


def pytest_addoption(parser):  # This will get the value from CLI /hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")


########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'RideCell Assignment'
    config._metadata['Module Name'] = 'Django GitHub'
    config._metadata['Tester'] = 'Ameya Natu'
