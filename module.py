# -*- coding: latin-1 -*-
##########
# Classes
##########
class Competitor:

    def __init__(self, gName):
        self.name = gName.lower()
        self.sports = [] #intialize empty

    def newSport(self, gSport):
        self.sports.append(gSport)

    def printResults(self): 
        print(self.name.title(),":",sep="")
        for reviewSport in self.sports :
            reviewSport.results() # call results mehtods

class Sport:#further development

    league = "" 
    def results(self):
        print(">>", self.league,  "<<")

class Run (Sport):

    def __init__(self, gLeague, gDistance, gTime):
        self.league = gLeague
        self.distance = gDistance
        self.time = gTime

    def results(self):
        Sport.results(self)
        if self.distance <= 800:
            print(self.distance, "meters in", self.time, "seconds")
        else:
            print(self.distance, "meters in", self.time, "mintues")
			
class Longjump (Sport):

    def __init__(self, gLeague, gLongjump):
        self.league = gLeague
        self.ljumps = gLongjump

    def results(self):
        Sport.results(self)
        best = -1
        print("Jumps:", end=" ")
        for reviewLj in self.ljumps :
            print(reviewLj, end=" ")
            if reviewLj > best :
                best = reviewLj
        print("--->> Best:", best)

class Walking (Sport):

    def __init__(self, gDistance, gTime):
        self.league = "Casual walking"
        self.distance = gDistance
        self.time = gTime

    def results(self):
        Sport.results(self)
        print(self.distance, "meters in", self.time, "minutes")

class Pullup (Sport):

    def __init__(self, gLeague, gPullups):
        self.league = gLeague
        self.pullups = gPullups

    def results(self):
        Sport.results(self)
        print(self.pullups, "pull-ups")