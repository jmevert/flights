from multiprocessing import Process

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from bs4 import BeautifulSoup

import time

class Request(Process):

    def __init__(self, url):
        options = Options()
        options.set_headless(headless=True)
        self.firefox = webdriver.Firefox(firefox_options=options, executable_path="/usr/local/bin/geckodriver")
        self.url = url
        Process.__init__(self)

    def getPrice(result):
        price_div = result.find("div", attrs={"class": "au-target c-flights_result_result_ticket-aside-price-label has-cursor_pointer"})
        price = price_div.get_text()[:-4]
        return int(price)

    def run(self):
        # GET URL AND DELAY FOR 30 SECONDS AFTERWARDS
        print("Getting URL ...")
        self.firefox.get(self.url.getString())
        print("Got URL, delay 30 seconds to ensure that the page is fully loaded ...")
        time.sleep(30)

        # GET HTML
        html = self.firefox.page_source

        # GET FLIGHT SEARCH RESULTS
        parsed_html = BeautifulSoup(html, "html.parser")

        results = parsed_html.body.find_all("div", attrs={"class": "c-flights_result_result-ticket"})
        prices = []

        for result in results:
            price = self.getPrice(result)
            prices.append(price)

        prices.sort()
        print("")
        print("TRAVEL FROM " + self.url.getOrigin() + " TO " + self.url.getDestination() + ".")
        print("LOWEST PRICE: " + str(prices[0]) + " EUR")
