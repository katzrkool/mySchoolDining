import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import datetime as theCENTER
import os

doIExist = True

#tries to open prefrences and set schoolName and menuSelection variables
try:
    with open("{}/preferences.json".format(os.path.dirname(__file__)),"r") as f:
        preferences = json.load(f)
        schoolName = preferences["schoolName"]
        try:
            menuSelection = preferences["menu"]
        except:
            pass
#if not it asks for the school name and verifies that it exists
except:
    doIExist = False
    schoolName = input("What's your myschooldining code? Found after the url on their site. \nExample: For myschooldining.com/thenewschool, thenewschool would be your code\n")
    while True:
        soup = BeautifulSoup(requests.get("http://myschooldining.com/{}".format(schoolName)).text,"html.parser")
        try:
            if soup.h1.text == "Hmm...doesn't look like that's here...":
                schoolName = input("That's not a valid code. Please try again.\t")
        except:
            break

#puts the menu in soup thing
soup = BeautifulSoup(requests.get("http://myschooldining.com/{}".format(schoolName)).text, "html.parser")
def pickMenuSelector():
    global menuSelection
    #finds the button div
    menuCenter = soup.findAll("span", attrs={"class":"section-title"})
    menuCenter = menuCenter[1]
    #finds the buttons
    button = menuCenter.findAll("button", attrs={"class":"change-school"})
    #if 1 button, use that button
    if len(button) == 1:
        date = determineWhichMenuToGrab()
        litButton = button[0].get("id")
        formatAndPrintDatData(litButton, date)
    #if more button, ask user which button to use
    else:
        if doIExist == False:
            for i in range(0,len(button)):
                print("{}. {}".format(i+1, button[i].text))
            menuSelection = int(input("Which menu do you want? Type in the number next to your chosen menu\t")) -1
        litButton = button[menuSelection].get("id")
        date = determineWhichMenuToGrab()
        formatAndPrintDatData(litButton, date)


def determineWhichMenuToGrab():
    todayzers = datetime.today().hour
    datezers = datetime.today()
    if datetime.today().weekday() == 6 or datetime.today().weekday() == 5:
        while datezers.weekday() != 0:
            datezers += theCENTER.timedelta(1)
    elif todayzers > 12 and datezers.weekday() != 4:
            datezers += theCENTER.timedelta(1)
    elif todayzers > 12 and datezers.weekday() == 4:
        while datezers.weekday() != 0:
            datezers += theCENTER.timedelta(1)
    elif todayzers <= 12:
        pass
    return datezers

def formatAndPrintDatData(litbutton,date):
    #what day is it?
    day = str(date.day)
    #sets up classes
    day = "day-" + day
    menuClass = "menu-"+litbutton
    #finds the menu location
    menu = soup.find("div", class_="{} {} menu-location".format(day, menuClass))
    #finds all menu items
    menu = menu.findAll("span", class_="no-print")
    #if its a category, get rid of it.
    menu = [i for i in menu if not i["class"] == ["month-category","no-print"]]
    #no more whitespace and print everything
    for i in range(0,len(menu)):
        menu[i] = menu[i].text
        menu[i] = menu[i].replace("\xa0", "")
        menu[i] = menu[i].replace("\n","")
        menu[i] = menu[i].replace("                             ","")
        print(menu[i])
    #ask to save info if info doesn't exist
    if doIExist == False:
        choice = "Netscape Navigator"
        while choice != "y" and choice != "n":
            choice = input("\nWould you like to save your info so you won't have to enter it next time? (y/n)").lower()
        if choice == "y":
            saveDatData()

#save data
def saveDatData():
    with open("{}/preferences.json".format(os.path.dirname(__file__)),"w") as fp:
        try:
            json.dump({"schoolName":schoolName, "menu":menuSelection}, fp)
        except:
            json.dump({"schoolName":schoolName}, fp)
pickMenuSelector()
