class URL:

    def __init__(self, attributes):
        self.origin = attributes["origin"]
        self.destination = attributes["destination"]
        self.url = "https://www.momondo.de/fluege/search/" + attributes["origin"] + "/" + attributes["destination"] + "/" + attributes["date1"] + "/" + attributes["date2"] + "?tc=eco&na=false&ac=2&dp=false&route_referrer=searchform&a=0.9966664888332134"

    def getString(self):
        return self.url

    def getOrigin(self):
        return self.origin

    def getDestination(self):
        return self.destination
