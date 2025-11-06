"""
Exercise 106: Remove outliers
Write a function that takes a list of nums and returns w the smallest and largest removed
"""

def removeOutliers (intsList):
    intsList.sort()
    del intsList[len(intsList)-1]
    del intsList[0]
    return intsList

trialList = [1,10,15,7,4,203]
#print(removeOutliers(trialList))

"""
Exercise 112: Below and above avg
Write a function that reads numbers until a blank line is entered and calculates the avg and 
whether values in the list are greater than or less than the avg
"""

def getList():
    intList = []
    num = "nothing"
    while num != "":
        num = input("Number: ")
        intList.append(num)
    del intList[len(intList)-1]
    return intList


def getAvg(numlist):
    listsum = 0
    for i in range(len(numlist)):
        listsum += int(numlist[i])
    avg = listsum/len(numlist)
    return avg

def greaterLess(numlist):
    greaterList = []
    lessList = []
    average = getAvg(numlist)
    for i in range(len(numlist)):
        if float(numlist[i])>average:
            greaterList.append(numlist[i])
        elif float(numlist[i])<average:
            lessList.append(numlist[i])
    print("Average:",average)
    print("Greater than average:", greaterList)
    print("Less than average:", lessList)

#greaterLess(trialList)
#greaterLess(getList())

"""
Exercise 111:
Identifies all words in a string and returns a list of words with punctuation removed 
"""

def splitText(string):
    cleanString = ""
    for char in string:
        if char not in ("!@#$%^&*()_-+=~`{[]}|\:;,<.>?/"):
            #if (char != "!") & (char != ",") & (char != "."):
            cleanString += char
        else:
            continue
    splitList = cleanString.split()
    return splitList

print(splitText("Hi! I'm, Briana."))