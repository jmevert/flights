from url import URL

class Date:
    ANY = "Any"

class Origin:
    ALL = "ALL_ORIGINS"
    ORIGINS = []
    @classmethod
    def initAllOrigins(cls, json):
        Origin.ORIGINS = json["origins"]
    @classmethod
    def getAllOrigins(cls):
        return Origin.ORIGINS

class Travel:

    def __init__(self, json):
        self.origin = json["origin"]
        self.destinations = json["destinations"]
        self.startDate = json["startdate"]
        self.endDate = json["enddate"]
        self.setupURLs()

    def setupURLs(self):
        self.urls = []
        origins = self.getOrigins()
        destination = self.destinations[0]
        for origin in origins:
            startdate = self.getStartDate()
            enddate = self.getEndDate()
            url = URL({"origin": origin, "destination": destination, "date1": startdate, "date2": enddate})
            self.urls.append(url)

    def getURLs(self):
        return self.urls

    def getOrigins(self):
        if self.origin == Origin.ALL:
            return Origin.getAllOrigins()
        else:
            return [self.origin]

    def getStartDate(self):
        return "2018-6-1"

    def getEndDate(self):
        return "2018-6-5"
