#Functions are either void or fruitful
import math

#Global variability
global f_name

#Void function
def setName(fname):
    f_name.set(fname)
    print(fname)

def getName():
    #fname is the local function variable, f_name is the global variable
    return f_name

"""
sum(list of numbers)
function adds all numeric values in a list
return int sum
"""
def sum(numbers):
    sum = 0
    for i in range (len(numbers)):
        sum+=numbers[i] #same as sum=sum+numbers[i]
    return sum
    #you can return any datatype, but only one return statement per function

test1 = [100,120,24,24,2345,233,89]
#print(sum(test1))

# Fruitful func to compare 2 nums
# Returns largest

def greaternum (num1,num2):
    if num1>num2:
        return num1
    elif num2>num1:
        return num2
    elif num1==num2:
        return num1
    else:
        return "Invalid"

print(greaternum(2,9))
# Fruitful func that returns value of hypotenuse 
# given a and b

def hypotenuse(a,b):
    c2 = a**2+b**2
    c = math.sqrt(c2)
    return c

print(hypotenuse(3,4))
# Fruitful func to find slope given 2 points

def slope(x1,x2,y1,y2):
    rise = y2-y1
    run = x2-x1
    slope = rise/run
    return slope

print(slope(3,4,5,6))
# Fruitful func that finds y-int given 2 points
# Should call slope func to calculate y int or b val

def y_int(x1,x2,y1,y2):
    b = y1-(slope(x1,x2,y1,y2)*x1)
    return b

print(y_int(3,4,5,6))
# Fruitful func that calculates whether a num is a factor 
# of another num
# Ex: is 3 a factor of 9?
def factor(a,b):
    if b%a == 0:
        return True
    elif b%a > 0:
        return False

print(factor(3,9))
# Fruitful func that determines whether a number is a multiple of another
def mult(a,b):
    if a%b == 0:
        return True
    elif a%b > 0:
        return False
    
print(mult(3,9))