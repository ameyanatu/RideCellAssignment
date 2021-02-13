import json

with open("./configuration_files/config.json", 'r') as configFile:
    data = configFile.read()

obj = json.loads(data)


class ReadConfig:
    @staticmethod
    def getDjangoWebURL():
        url = obj['DjangoGitHubPageURL']
        return url

    @staticmethod
    def getDjangoAPI():
        API_EndPoint = obj['DjangoGithubGETEndpoint']
        return API_EndPoint
