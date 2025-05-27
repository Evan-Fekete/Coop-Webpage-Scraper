import requests
from bs4 import BeautifulSoup
# from requests.auth import HTTPBasicAuth

# basic = HTTPBasicAuth('root', 'evertz')

''' PUT URL HERE '''
URL = "https://realpython.github.io/fake-jobs/"

page = requests.get(URL) # requests.get(URL, auth=basic) for login

print(page.content, "html.parser")