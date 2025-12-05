mylist =[]
userInput = 1
while userInput != 0:
    userInput = int(input("Enter an int"))
    mylist.append(userInput)
mylist.pop(len(mylist)-1)
print(mylist)