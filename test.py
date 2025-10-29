import math
# Number 1 (Truth tables)
# Original answers were correct
def truth (a,b,c):
    if ((a and (b or c))==True):
        return True
    else:
        return False
    
#1
print(truth(False, False, False)) 
#2
print(truth(False, False, True))
#3
print(truth(False, True, False))
#4
print(truth(False, True, True))
#5
print(truth(True, False, False))
#6
print(truth(True, False, True))
#7
print(truth(True, True, False))
#8
print(truth(True, True, True))

# Number 2 (Program that calculates area)
# Did not have to make any changes to handwritten code
def getRadius():
    radius = float(input("What is the radius? "))
    return radius

def areaCircle(radius):
    area = math.pi * radius**2
    return area

print(areaCircle(getRadius()))

# Number 3 (Password guesser)
trialPassword = "myPass"
def getPassword(password):
    attempt = str(input("What is the password? "))
    if attempt == password: 
        return True
    else:
        return False

# This does not work
def passAttempt(password):
    i=0
    while  i>3:
        if getPassword(password)==True:
            print("You have successfully logged in.")
            i=4
        elif getPassword(password)==False:
            i+=1
    if i!=4:
        print("You have been denied access.")

#passAttempt(getPassword(trialPassword))

# Corrected function
def passAttemptNew(password):
    for i in range (2):
        if getPassword(password):
            print("You have successfully logged in.")
            return "You have successfully logged in. "
        else:
            print("You have been denied access.")
            return "You have been denied access."

passAttemptNew(trialPassword)
        
