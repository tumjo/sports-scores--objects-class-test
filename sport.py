# -*- coding: latin-1 -*-
from modulefunc import addCompetitor, searchCompetitor, addRun, addLongjump, addWalking, addPullup, printComp
################
# User interface
################
def menu():
    print("==================")
    print("MENU")
    print("c  Add competitor")
    print("r  Add run")
    print("l  Add long jump")
    print("w  Add walking")
    print("p  Add pull-up")
    print("pr Print the results on screen")
    print("q  Quit")          
    print("==================")

def mainloop(cl):
    print("The scoreboard has been launched")
    menu()
    while True:
        selection = input("Select: ")
        if (selection == 'c'):
            addCompetitor(cl)
        elif (selection == 'r'):
            addRun(cl)
        elif (selection == 'l'):
            addLongjump(cl)
        elif (selection == 'w'):
            addWalking(cl)
        elif (selection == 'p'):
            addPullup(cl)
        elif (selection == 'pr'):
            printComp(cl)
        elif (selection == 'q'):
            break
        else: #unidentified command
            print("Unidentified command")
            menu()
######
# Main
######
clist = []
mainloop(clist)
