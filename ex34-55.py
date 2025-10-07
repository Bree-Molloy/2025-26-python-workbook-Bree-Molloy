
"""
Exercise 34: Even or Odd?
Write a program that reads an integer from the user.
Then your program should display a message indicating whether
the integer is even or odd
"""
def evenOdd():
    num = input("What is the number?")
    if int(num)%2 == 0:
        return "Number is even"
    elif int(num)%2 != 0:
        return "Number is odd"
    else:
        return "Not a number"

#print(evenOdd())

"""
Exercise 36: Vowel or consonant
In this exercise you will create a program that reads a letter
of the alphabet from the user. If the user enters a, e, i, o, or u
then your program should display a message indicating that the
entered letter is a vowel. If the user enters y then your program
should display a message indicating that sometimes y is a vowel, and
sometimes y is a consonant. Otherwise your program should display
a message indicating that the letter is a consonant.
"""
def vowelConsonant():
    letter = input("Letter:")
    letter = letter.upper()
    if len(letter) > 1:
        return "Invalid input"
    elif letter == ("A" or "E" or "I" or "O" or "U"):
        return "Letter is a vowel"
    else:
        return "Letter is a consonant"

#print(vowelConsonant())

"""
Exercise 40: Name that triangle
A triangle can be classified based on the lengths of its sides as
equilateral, isosceles, or scalene. All 3 sides of an equilateral
triangle have the same length. As isosceles triangle has two sides
that are the same length, and a third side that is a different length.
If all of the sides have different lengths then the triangle is scalene.
Write a program that reads the lengths of 3 sides of a triangle from the
user. Display a message indicating the type of triangle
****** CHALLENGE:
Perform the same task as above but with angles and not sides.
"""
def triangleNameSideLength():
    l1 = float(input("Side 1 length:"))
    l2 = float(input("Side 2 length:"))
    l3 = float(input("Side 3 length:"))
    if ((l1 == l2) and (l2 == l3)):
        return "Triangle is equilateral"
    elif ((l1 == l2) or (l1 == l3) or (l2==l3)):
        return "Triangle is isosceles"
    elif (l1 != l2) and (l1 != l3) and (l2 != l3):
        return "Triangle is scalene"
    else:
        return "Invalid input"
    
def triangleNameAngle():
    a1 = float(input("Angle 1 measure:"))
    a2 = float(input("Angle 2 measure:"))
    a3 = float(input("Angle 3 measure:"))
    if ((a1 == a2) and (a2 == a3) and (a1+a2+a3 == 180)):
        return "Triangle is equilateral"
    elif (((a1 == a2) or (a1 == a3) or (a2==a3)) and (a1+a2+a3 == 180)):
        return "Triangle is isosceles"
    elif ((a1 != a2) and (a1 != a3) and (a2 != a3) and (a1+a2+a3 == 180)):
        return "Triangle is scalene"
    else:
        return "Invalid input"        
#print (triangleNameSideLength())
#print (triangleNameAngle())
"""
Exercise 55: Cell Phone Bill
A particular cell phone plan includes 50 minutes of air time and
50 text messages for $15.00 a month. Each additional minute of
air time costs $0.25 , while additional text messages cost $0.15
each. All cell phone bills include an additional charge of $0.44
to support 911 call centers, and teh entire bill (including the
911 charge) is subject to a 5 percent sales tax.
Write a program that reads the number of minutes and text messages
used in a month from the user. Display the base charge, additional
minutes charge (if any), additional text message charge (if any),
the 911 fee, tax and total bill amount. Only display the additional
minute and text charges if the user incurred costs in these
categories. Ensure that all of the charges are displayed using 2
decimal points
"""
def cellPhoneBill():
    minutes = float(input("Minutes:"))
    texts = float(input("Text messages:"))
    total = 15.44
    extraMinCharge = 0
    extraTextCharge = 0
    if minutes > 50:
        total = total + .25*(minutes-50)
        extraMinCharge = .25*(minutes-50)
    if texts > 50:
        total = total + .15*(texts-50)
        extraTextCharge = .15*(texts-50)
    tax = total*.05
    total = tax + total
    print("Initial Charge: $15.00")
    if (extraMinCharge != 0 and extraTextCharge != 0):
        print("Extra minutes charge: $"+str(round(extraMinCharge,2)))
        print("Extra text charge: $"+str(round(extraTextCharge,2)))
    elif (extraMinCharge != 0):
        print("Extra minutes charge: $"+str(round(extraMinCharge,2)))
    elif (extraTextCharge != 0):
        print("Extra text charge: $"+str(round(extraTextCharge,2)))
    print("911 fee: $0.44")
    print("Tax: $"+ str(round(tax,2)))
    print("Total: $"+ str(round(total,2)))

cellPhoneBill()
