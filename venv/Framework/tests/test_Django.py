import pytest
from selenium import webdriver
import utilities.customLogger as cl
from utilities.readConfigFile import ReadConfig
from POM.Django_github_page import DjangoPage
from POM.Django_github_API import DjangoAPI
import logging


class Test_DjangoData:

    DjangoURL = ReadConfig.getDjangoWebURL()
    DjangoAPIEndPoint = ReadConfig.getDjangoAPI()
    log = cl.customLogger(logging.DEBUG)

    def test_Django_Data(self, setup):
        self.log.info("Testing Django Data Validation****")
        self.driver = setup
        self.log.info("Opening URL")
        self.driver.get(self.DjangoURL)
        self.driver.maximize_window()
        self.DP = DjangoPage(self.driver)
        self.DP.clickOnRepo()
        self.log.info("Getting Repository Data From Github Web page")
        WebJSONData = self.DP.getRepositoryData()
        self.driver.close()
        self.DA = DjangoAPI()
        self.log.info("Getting Repository Data From Github GET API Endpoint")
        APIJSONData = self.DA.getRepositoryDataAPI(self.DjangoAPIEndPoint)
        self.log.info("Asserting Actual Data with Expected Data")
        assert WebJSONData == APIJSONData



