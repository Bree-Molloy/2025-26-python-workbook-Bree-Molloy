
"""
Exercise 108: Negatives, Zeros, and Positives
Create a program that reads integers from the user until a blank
line is entered. 

Once all of the integers have been read your program should display
all the negative numbers, followed by all of the zeros, followed by 
all of the positive numbers. 

Within each group the numbers should be displayed in the same order 
that they were entered by the user. 

For example, if the user enters the values
3, -4, 1, 0, -1, 0, and -2 then your program should output the values
-4, -1, -2, 0 ,0 , 3, and 1. Your program should display each value
on its own line.
"""
#Reads integers until a blank line is entered
def getInts():
    intList = []
    int = "nothing"
    while int != "":
        int = input("Number: ")
        intList.append(int)
    return intList

#Sorts the list in order and prints the values
def orderList(listofints):
    listofints.sort() 
    for i in range (len(listofints)):
        print (listofints[i])
    return listofints
    
orderList(getInts())


"""
Exercise 109: List of Proper Divisors
A proper divisor of a positive integer, n, is a positive integer
less than n which divides evenly into n. Write a function that
computes all of the proper divisors of a positive integer. The
integer will be passed to the function as its only parameter.
The function will return a list containing all of the proper divisors
as its only result. Complete this exercise by writing a main program
that demonstrates the function by reading a value from the user and
displaying the list of its proper divisors. Ensure that your main
program only runs when your solution has not been imported into
another file
"""
def getPosInt():
    posInt = int(input("What is the number? "))
    return posInt

def divisorsList(int):
    divList = []
    for i in range (int):
        if i==0:
            continue
        elif int%i == 0:
            divList.append(i)
    return divList

print(divisorsList(64))
print(divisorsList(256))
print(divisorsList(getPosInt()))

"""
Exercise 110: Perfect Numbers
An integer, n, is said to be perfect when the sum of all the proper
divisors of n is equal to n. For example, 28 is a perfect number
because its proper divisors are 1, 2, 4, 7, and 14, and 1+2+4+7+14 = 28.
Write a function that determines whether or not a positive integer is
perfect. Your function will take one parameter. If that parameter is a
perfect number then your function will return true. Otherwise it will
return false. In addition, write a main program that uses your
function to identify and display all of the perfect numbers between 1 and
10,000. Import your solution to Exercise 109 when completing this task.
"""

def isPerfectNum(num):
    sumOfFactors = 0
    factorList = divisorsList(num)
    for i in range (len(factorList)):
        sumOfFactors += factorList[i]
    if num == sumOfFactors:
        return True
    else:
        return False
    

def perfNums():
    perfNumsList = []
    for i in range(10000):
        if isPerfectNum(i):
            perfNumsList.append(i)
    return perfNumsList

print(perfNums())