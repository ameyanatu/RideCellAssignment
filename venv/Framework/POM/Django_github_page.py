from selenium import webdriver
import json
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
import utilities.customLogger as cl
import logging


class DjangoPage:

    log = cl.customLogger(logging.DEBUG)
    repo_link_xpath = "//*[@class='UnderlineNav-item selected']"
    repo_list_xpath = "//*[@class = 'org-repos repo-list']/ul/li"
    individual_repo_name_xpath = ".//a[contains(@itemprop, 'name')]"
    individual_repo_description_xpath = ".//p[contains(@itemprop, 'description')]"

    def __init__(self, driver):
        self.driver = driver

    def clickOnRepo(self):
        try:
            self.driver.find_element_by_xpath(self.repo_link_xpath).click()
            self.log.info("Django Repository Link is Clicked")
        except NoSuchElementException as exception:
            self.log.error("Repository Link Element is Not Found")
        except ElementNotVisibleException as exception:
            self.log.error("Repository Link Element is Not Visible")

    def getRepositoryData(self):
        try:
            repo_list = self.driver.find_elements_by_xpath(self.repo_list_xpath)
            Web_Data_Json = dict()
            for repo in repo_list:
                repo_name = repo.find_element_by_xpath(self.individual_repo_name_xpath).text
                # Description is optional therefore checking description element is present or not.
                if len(repo.find_elements_by_xpath(self.individual_repo_description_xpath)) > 0:
                    Web_Data_Json[repo_name] = repo.find_element_by_xpath(self.individual_repo_description_xpath).text
                else:
                    Web_Data_Json[repo_name] = None
            return Web_Data_Json
        except NoSuchElementException as exception:
            self.log.error("Individual Repository Element is Not Found")
        except ElementNotVisibleException as exception:
            self.log.error("Individual Repository Element is Not Visible")
