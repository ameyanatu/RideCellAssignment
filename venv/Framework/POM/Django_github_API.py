import requests
import json
import utilities.customLogger as cl
import logging


class DjangoAPI():
    log = cl.customLogger(logging.DEBUG)

    def __init__(self):
        self.log.info("Django API Class initiated")

    def getRepositoryDataAPI(self, URL):
        API_Data_JSON = dict()
        response = requests.get(URL)
        responseList = response.json()
        for repo in responseList:
            API_Data_JSON[repo['name']] = repo['description']
        return API_Data_JSON
