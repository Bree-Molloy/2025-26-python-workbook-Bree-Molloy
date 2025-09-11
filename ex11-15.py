import math
"""
Exercise 11: Fuel Efficiency
In the United States, fuel efficiency for vehicles is normally expressed
in miles-per-gallon (MPG).  In Canada, fuel efficiency is normally
expressed in liters-per-hundred_kilometers (L/100km).  Use your 
research skills to determine how to convert from MPG to L/100km.
Then create a program that reads a value from the user in American units
and display the equivalent fuel efficiency in Canadian units.
"""
def fuelEfficiency():
    mpg = str(input("MPG:"))
    lper100km = 235.215/mpg
    print("It is ",lper100km,"L/100km")
fuelEfficiency()

"""
Exercise 12:  Distance Between Two Points on Earth
The surface of the Earth is curved, and teh distance between degrees
of longitude varies with latitude.  As a result, finding the distance
between two points on the surface of the Earth is more complicated than 
simply using the Pythagorean theorem.

Let (t1,g1) and (t2,g2) be the latitude and longitude of two points on the
Earth's surface.  The distance between these points, following the 
surface of the Earth, in kilometers is:

distance = 6371.01 x arccos(sin(t1) x sin(t2) + cos(t1) x cos(t2) x cos(g1-g2))

*** The value 6371.01 in the previous equation wasn't selected at random.
It is the average radius of the EArth in kilometers. ***

Create a program that allows the user to enter the latitude and longitude
of two points on the Earth in degrees.  Your program should display the 
distance between the points, following the surface of the earth, in km.

*** HINT ***
Python's trigonometric functions operate in radians.  As a result, you will
need to convert the user's input from degrees to radians before computing
the distance with the formula discussed previously.  The math module 
contains a function named RADIANS which converts from degrees to radians.
"""
def distanceEarth():
    t1 = math.radians(float(input("t1:")))
    g1 = math.radians(float(input("g1:")))
    t2 = math.radians(float(input("t2:")))
    g2 = math.radians(float(input("g2:")))
    distance = (math.sin(t1) * math.sin(t2) + math.cos(t1) * math.cos(t2) * math.cos(g1-g2))
    distance = math.acos(distance)
    distance = distance*6371.01
    print (distance)

distanceEarth()
"""
Exercise 13: Making Change
Consider the software that runs on a self-checkout machine.  One task that
it must be able to perform is to determine how much change to provide 
when the shopper pays for a purchase with cash.

Write a program that begins by reading a number of cents from the user
as an integer.  Then your program should compute and display the 
denominations of the coins that should be used to give that amount 
of change  to the shopper.  The change should be given using as 
few coins as possible.  Assume that the machine is loaded with pennies,
nickels, dimes, quarters, loonies and toonies.

*** A one dollar coin was introduced in Canada in 1987  It is referred
to as a loonie because one side of the coin has a loon (type of bird) on it.
The two dollar coin, referred to as a toonie, was introduced 9 years later.
It's name is derived from the combination of the number two
and the name of the loonie.
"""

def nCents():  
    cents = int(input("How many cents? "))      
    toonie = cents//200
    cents = cents-(toonie*200)
    loonie = cents//100
    cents = cents-(loonie*100)
    quarters = cents//25
    cents = cents-(quarters*25)
    dimes = cents//10
    cents = cents-(dimes*10)
    nickels = cents//5
    cents = cents-(nickels*5)
    pennies = cents
    print("Toonies:", toonie)
    print("Loonies:", loonie)
    print("Quarters:", quarters)
    print("Dimes:", dimes)
    print("Nickels:", nickels)
    print("Pennies:", pennies)

nCents()


"""
Exercise 14:  Height Units
Many people think about their height in feet and inches, even in some
countries that primarily use the metric system.
Write a program that reads a number of feet from the user, followed 
by a number of inches.  Once the values are read, your program should 
compute and display the equivalent number of centimeters.

*** HINT ***
One foot is 12 inches.  One in ch is 2.54 centimeters.
"""
def heightUnits():
    nFeet = int(input("How many feet? "))
    nInches = int(input("How many inches? "))
    nInches = nInches+(nFeet*12)
    centimeters = nInches*2.54
    print("Centimeters=", centimeters)
heightUnits()

"""
Exercise 15:  Distance Units
In this exercise, you will create a program that begins by reading
a measurement in feet from the users.  Then your program should display
the equivalent distance in inches, yards, and miles. 

*** HINT ***
1 inch = 0.02777778 yards = 0.00001578 miles
36 inches = 1 yard = 0.00056818 miles
63360 inches = 1760 yards = 1 mile
"""
def distanceUnits():
    feet = int(input("How many feet? "))
    inches = feet*12
    yards = inches*0.02777778
    miles = inches*0.00001578
    print("Inches:", inches)
    print("Yards:", yards)
    print("Miles:", miles)

distanceUnits()

