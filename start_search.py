from travel import *
from request import *

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from bs4 import BeautifulSoup

import json
import time

try:
    with open("travels.json", "rb") as f:
        json = json.loads(f.read())
        Origin.initAllOrigins(json)
except IOError as err:
    print("An error occured: " + str(err))

travels = []

for travel_node in json["travels"]:
    travel = Travel(travel_node)
    travels.append(travel)

for travel in travels:
    for url in travel.getURLs():
        request = Request(url)
        request.start()
