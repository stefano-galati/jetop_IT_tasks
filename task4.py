from sys import exit
from pprint import pprint
import datetime

FILENAME = "input.txt"

def importDate():
    x = datetime.date.today()
    return x

def modifyAndSortList(listOfLines):
    #remove lines before the current day

    today = importDate()
    counter = 0

    while counter<len(listOfLines):
        tempDate = listOfLines[counter]["date"]
        tempDate = datetime.date(int(tempDate[2]), int(tempDate[1]), int(tempDate[0]))
        if(tempDate<today):
            listOfLines.pop(counter)
        else:
            counter += 1

    #sort list according to date
    newList = sorted(listOfLines, key=lambda x: datetime.date(int(x["date"][2]), int(x["date"][1]), int(x["date"][0])))
    return newList


def printElement(elementDict):
    #write data as day-month-year
    tempDate=str(f"{elementDict['date'][0]}-{elementDict['date'][1]}-{elementDict['date'][2]}")
    #print formatted output
    print(f"{elementDict['name']:<30} {tempDate:<15} {elementDict['room']:<5}")

def readFileAndCreateDict(file):
    listOfLines = list()

    try:
        with open(file, "r") as inputFile:
            for line in inputFile:
                line = line.rstrip().split(";")
                dictLine = dict()
                dictLine["name"] = line[0]
                dictLine["date"] = line[1].split('/')
                dictLine["room"] = line[2]
                listOfLines.append(dictLine)

    except FileNotFoundError:
        exit(1)

    return listOfLines


def main():
    #create list of dictionaries
    listOfLines = readFileAndCreateDict(FILENAME)

    newList = modifyAndSortList(listOfLines)

    print("Scrivi STOP per terminare il programma")
    userInput = input("Area da considerare: ")
    while(userInput.lower()!="stop"):
        #find the asked data in the list of dictionaries
        for element in newList:
            temp = element["name"].lower().split()
            if (userInput.lower() in temp) or ("generale" in temp):
                printElement(element)
        userInput = input("Area da considerare: ")




if __name__ == '__main__':
    main()
