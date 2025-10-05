import math
"""
Exercise 21:  Area of a Triangle
The area of a triangle can be computed using the following formula,
where b is the length of the base of the triangle, and h is its 
height:
        area = (b*h)/2
Write a program that allows the user to enter values for b and h.
The program should then compute and display the area of a triangle
with base length b and height h
"""
def areaTriangle():
    b = float(input("Base:"))
    h = float(input("Height:"))
    area = (b*h)/2
    print("Area:"+str(area))

#areaTriangle()
"""
Exercise 22: Area of a triangle (Again)
In the previous exercise you created a program that computed the area
of a triangle when the length of its base and its height were known.
It is also possible to compute the area of a triangle when the lengths
of all three sides are known.  Let s1, s2, and s3 be the lengths of the
sides.  Let s = (s1 + s2 + s3)/2.  Then the area of a triangle can be 
calculated using the following formula:

     area = (s * (s - s1) * (s - s2) * (s - s3))**(1/2)

Develop a program that reads the lengths of the sides of a triangle from
the user and display its area.
"""
def areaTriangle2():
    s1 = float(input("Side 1 length:"))
    s2 = float(input("Side 2 length:"))
    s3 = float(input("Side 3 length:"))
    s = (s1 + s2 + s3)/2
    area = (s * (s - s1) * (s - s2) * (s - s3))**(1/2)
    print("Area:"+str(area))

#areaTriangle2()

"""
Exercise 23:  Area of a Regular Polygon
A polygon is regular if its sides are all the same length and the angles
between all of the adjacent sides are equal.  The area of a regular polygon
can be computed using the following formula, where s is the length of a side
and n is the number of sides: 
     area = (n * s**(2))/(4 * tan(pi/n))
Write a program that reads s and n from the user and then displays the area
of a regular polygon constructed from these values.
"""
def areaPolygon():
    n = int(input("Number of sides: "))
    s = float(input("Side length: "))
    area = (n * s**(2))/(4 * math.tan(math.pi/n))
    print("Area:"+str(area))

#areaPolygon()

"""
Exercise 24: Units of Time
Create a program that reads a duration from the user as a number of days,
hours, minutes, and seconds.  Compute the total number of seconds represented
by this duration.
"""
def unitsTime():
    days = int(input("Number of days:"))
    hours = int(input("Number of hours:"))
    minutes = int(input("Number of minutes:"))
    seconds = int(input("Number of seconds"))
    seconds = seconds+(days*24*3600)
    seconds = seconds + (hours*3600)
    seconds = seconds+(minutes*60)
    print(str(seconds)+" seconds")

#unitsTime()

""" 
Exercise 25: Units of Time (again)
In this exercise you will reverse the process described in the previous 
exercise.  Develop a program that begins by reading a number of seconds from 
the user.  Then your program should display the equivalent amount of time 
in the form D:HH:MM:SS, where D, HH, MM, and SS represent days, hours, 
minutes and seconds respectively.  The hours, minutes and seconds should all
be formatted so that they occupy exactly two digits, with a leading 0 displayed
if necessary.
"""
def unitsTime2():
    s = int(input("How many seconds? "))
    days = s//86400
    s = s-(days*86400)
    hours = s//3600
    s = s-(hours*3600)
    minutes = s//60
    s = s-(minutes*60)
    if len(str(hours))<2:
        hours = "0"+str(hours)
    if len(str(minutes))<2:
        minutes = "0"+str(minutes)
    if len(str(s))<2:
        s = "0"+str(s)
    print(str(days)+":"+str(hours)+":"+str(minutes)+":"+str(s))

unitsTime2()
