#Functions are either void or fruitful

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