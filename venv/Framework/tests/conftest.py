import pytest
import os
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    driver = ""
    if browser == 'chrome':
        driver = webdriver.Chrome()
        driver.maximize_window()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        driver.maximize_window()
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")



def pytest_configure(config):
    config._metadata['Project Name'] = 'RideCell Assignment'
    config._metadata['Module Name'] = 'Django GitHub'
    config._metadata['Tester'] = 'Ameya Natu'
