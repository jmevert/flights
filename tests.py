#from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from bs4 import BeautifulSoup

import time

def getURL(attributes):
    return "https://www.momondo.de/fluege/search/" + attributes["origin"] + "/" + attributes["destination"] + "/" + attributes["date1"] + "/" + attributes["date2"] + "?tc=eco&na=false&ac=2&dp=false&route_referrer=searchform&a=0.9966664888332134"

def getPrice(result):
    price_div = result.find("div", attrs={"class": "au-target c-flights_result_result_ticket-aside-price-label has-cursor_pointer"})
    price = price_div.get_text()[:-4]
    return int(price)

# DEFINITIONS
origin = "hamburg"
destination = "oslo"

date1 = "2018-6-1"
date2 = "2018-6-5"

# LOAD URL USING HEADLESS FIREFOX
url = getURL({"origin": origin, "destination": destination, "date1": date1, "date2": date2})

options = Options()
options.set_headless(headless=True)

firefox = webdriver.Firefox(firefox_options=options, executable_path="/usr/local/bin/geckodriver")

# GET URL AND DELAY FOR 30 SECONDS AFTERWARDS
print("Getting URL …")
firefox.get(url)
print("Got URL, delay 30 seconds to ensure that the page is fully loaded …")
time.sleep(30)

# GET HTML
html = firefox.page_source

# GET FLIGHT SEARCH RESULTS
parsed_html = BeautifulSoup(html, "html.parser")

results = parsed_html.body.find_all("div", attrs={"class": "c-flights_result_result-ticket"})
prices = []

for result in results:
    price = getPrice(result)
    prices.append(price)

prices.sort()
print("LOWEST PRICE: " + str(prices[0]) + " EUR")
