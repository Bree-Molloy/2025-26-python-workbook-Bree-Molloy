"""
Exercise 51: Letter Grade to Grade Points
At a particular university, letter grades are mapped to grade
points in the following manner:
Letter Grade points
A+ 4.0
A 4.0
A- 3.7
B+ 3.3
B 3.0
B- 2.7
C+ 2.3
C 2.0
C- 1.7
D+ 1.3
D 1.0
F 0
Write a program that begins by reading a letter grade from the
user. Then your program should compute and display the equivalent
number of grade points. Ensure that your program generates an
appropriate error message if the user enters an invalid letter
grade.
"""
#Global variables
A_PLUS = 4.0
A = 4.0
A_MINUS = 3.7
B_PLUS = 3.3
B = 3.0
B_MINUS = 2.7
C_PLUS = 2.3
C = 2.0
C_MINUS = 1.7
D_PLUS = 1.3
D = 1.0
F = 0
def getLetterGrade():
    #error catching
    letterGrade = input("What is your letter grade? ")
    letterGrade = letterGrade.upper()
    return letterGrade

def gradeToPoints(letterGrade):
    letterGrade = letterGrade.upper()
    if (letterGrade == "A+") or (letterGrade == "A"):
        numGrade = 4.0
    elif letterGrade == "A-":
        numGrade = 3.7
    elif letterGrade == "B+":
        numGrade = 3.3
    elif letterGrade == "B":
        numGrade = 3.0
    elif letterGrade == "B-":
        numGrade = 2.7
    elif letterGrade == "C+":
        numGrade = 2.3
    elif letterGrade == "C":
        numGrade = 2.0
    elif letterGrade == "C-":
        numGrade = 1.7
    elif letterGrade == "D+":
        numGrade = 1.3
    elif letterGrade == "D":
        numGrade = 1.0
    elif letterGrade == "F":
        numGrade = 0
    else:
        print ("Invalid input")
        numGrade = -1
    return numGrade

print(gradeToPoints(getLetterGrade()))
"""
Exercise 52: In the previous exercises you created a program that
converts a letter grade into the equivalent number of grade points.
In this exercise you will create a program that reverses the process
and converts from a grade point value entered by the user to a letter
grade. Ensure that your program handles grade point values that fall
between letter grades. These should be rounded to the closes letter
grade. Your program should report A+ for a 4.0 (or greater) grade
point average.
"""
def gpaToGrade():
    gpa = float(input("What is your GPA? "))
    if gpa >= A_PLUS:
        letterGrade = "A"
    elif gpa >= A_MINUS:
        letterGrade = "A-"
    elif gpa >= B_PLUS:
        letterGrade = "B+"
    elif gpa >= B:
        letterGrade = "B"
    elif gpa >= B_MINUS:
        letterGrade = "B-"
    elif gpa >= C_PLUS:
        letterGrade = "C+"
    elif gpa >= C:
        letterGrade = "C"
    elif gpa >= C_MINUS:
        letterGrade = "C-"
    elif gpa >= D_PLUS:
        letterGrade = "D+"
    elif gpa >= D:
        letterGrade = "D"
    elif gpa >= 0:
        letterGrade = "F"
    else:
        letterGrade = "Invalid input"
    return letterGrade
    
print (gpaToGrade())
"""
Exercise 66: Compute a Grade Point Average
Exercise 51 includes a table that shows the conversion from letter
grades to grade points at a particular academic institution. In this
exercise you will compute the grade point average of an arbitrary number
of letter grades entered by the user. The user will enter a blank
line to indicate that all of the grades have been provided. For example,
if the user enters A, followed by C+, followed by B, followed by a blank
line then your program should report a grade point average of 3.1.
You may find your solutions to Exercise 51 helpful when completing this
exercise. Your program does not need to do any error checking. It can
assume that each value entered by the user will be a valid letter grade
or a blank line.
"""
def getGrades():
    gradesList = []
    grade = "nothing"
    while grade != "":
        grade = input("What is the grade? ")
        gradesList.append(grade)
    return gradesList


def gpaCalculator(grades):
    gpa = 0
    for i in range(len(grades)-1):
        gpa += gradeToPoints(grades[i])
    gpa = gpa/(len(grades)-1)
    print(gpa)
    return gpa

gpaCalculator(getGrades())