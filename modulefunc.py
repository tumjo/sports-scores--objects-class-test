# -*- coding: latin-1 -*-
from module import Competitor, Sport, Run, Longjump, Walking, Pullup
###########
# Functions
###########
def addCompetitor(cl):
    newName  = input("Please enter a name: ")
    newCompetitor = Competitor(newName) #new Competitor object
    cl.append(newCompetitor)

def searchCompetitor(cl):
    competitorName  = input("Please enter the name: ")
    for competitor in cl :
        if competitor.name == competitorName.lower():
            return(competitor)
    print("No name found: ", competitorName)
    return(None)

def addRun(cl):
    runner = searchCompetitor(cl)
    if runner != None :
        league = input("Please enter the league: ")
        distance = int(input("Please enter the distance in meters: "))
        if distance<=800:
            time  = float(input("Please enter the time in seconds: "))
        else:
            time  = float(input("Please enter the time in minutes: "))
        newRun = Run(league, distance, time)
        runner.newSport(newRun)

def addLongjump(cl): 
    co = searchCompetitor(cl)
    if co != None :
        league = input("Please enter the league: ")
        ljumps = []
        print("Please enter five values")
        for i in range(5) :
            print("Please enter", i+1, ":", end = '')
            ljumps.append(float(input()))
        co.newSport(Longjump(league, ljumps))

def addWalking(cl):
    co = searchCompetitor(cl)
    if co != None :
        while True:
            distance = int(input("Please enter the distance in meters: "))
            if distance < 800:
                print("Please enter longer distance!")
            else:
                break
        time  = float(input("Please enter the time in minutes: "))
        newWalking = Walking(distance, time)
        co.newSport(newWalking)

def addPullup(cl):
    co = searchCompetitor(cl)
    if co != None :
        league = input("Please enter the league: ")
        pullups = int(input("Please enter the amount of pull-ups: "))
        newPullup = Pullup(league, pullups)
        co.newSport(newPullup)

def printComp(cl):
    co = searchCompetitor(cl)
    if co != None :
        co.printResults()

#def addExample(cl): #new sport
	#