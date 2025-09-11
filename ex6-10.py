import math
"""
Exercise 6: Tax and Tip
The program you create for this exercise will begin by reading the cost
of a meal ordered at a restaurant from the user.  Then your program will
compute the tax and tip for the meal.  Use your local tax rate when 
computing the amount of tax owing.  Compute the tip as 18 percent of  the 
meal amount (without tax).  The output from your program should include
both the tax and the tip.  Format the output so that all of the values
are displayed using two decimal places.  (17 lines)
"""
def mealPrice ():
    foodPrice = input("What did the food cost? ")
    tax = float(foodPrice)*.0575
    tip = float(foodPrice)*.18
    totalPrice = float(foodPrice)+tax+tip
    totalPrice = round(totalPrice,2)
    print("The price is $" + str(totalPrice))
mealPrice()

"""
Exercise 7:  Sum of the First n Positive Integers
Write a program that reads a positive integer, n, from the user and 
then displays the sum of all the integers from 1 to n.  The sum of the 
first n positive integers can be computed using the formula:
sum = (n*(n+1))/2
(12 lines)
"""
def sumOfPosInt ():
    n = input("What is the number? ")
    n = int(n)
    sum = (n*(n+1))/2
    print(sum)
sumOfPosInt()

"""
Exercise 8:  Widgets and Gizmos
An online retailer sells two products:   widgets and gizmos.  Each widget 
weighs 75 grams.  Each gizmo weighs 112 grams.  Write a program that reads
the number of gizmos in an order from the user.  Then your program should 
compute and display the total weight of the order.  (15 lines)

"""
def totalWeight():
    nWidgets = input("Number of widgets:")
    nGizmos = input("Number of gizmos:")
    weight = float(nGizmos)*112+float(nWidgets)*75
    print("Weight=" + str(weight) + " grams")
totalWeight()

"""
Exercise 9:  Compound Interest
Pretend that you have just opened a new savings account that earns 4 percent
interest per year.  The interest that you earn is paid at the end of the year, 
and is added to the balance of the savings account.  Write a program that begins
by reading the amount of money deposited into the account from the user.  Then 
your program should compute and display the amount in the savings account after
1, 2, and 3 years.  Display each amount so that it is rounded to 2 decimal 
places.  (19 lines)
"""
def compoundInterest():
    #P(1 + r/n)^(nt)
    p = float(input ("What is the principle value? "))
    r = float(input ("What is the interest rate? "))
    n = float(input ("How many times does it compound annually? "))
    t = float(input ("How many years? "))
    interest = p*(1 + r/n)**(n*t)
    print (interest)
    
compoundInterest()


    

"""
Exercise 10:  Arithmetic
Create a program that reads two integers, a and b, from the user.  Your program
should compute and display:
- the sum of a and b
- the difference when b is subtracted from a
- the product of a and b
- the quotient when a is divided by b
- the remainder when a is divided by b
- the result of log10 a
- the result of a to the power of b

Hint:  you will probably find the log10 function in the math module helpful
for computing the second last item in the list.
"""

def arithmetic():
    a = int(input("a="))
    b = int(input("b="))
    sum = a+b
    difference = a-b
    product = a*b
    quotient = a/b
    remainder = a%b
    log = math.log10(a)
    power = a**b
    print("Sum=", sum)
    print("a-b=", difference)
    print("Product=", product)
    print("a/b=", quotient)
    print("Remainder", remainder)
    print("log10a=", log)
    print("a^b=", power)

arithmetic()
