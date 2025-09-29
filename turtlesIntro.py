import turtle

# Create a turtle instance
# Creating a variable that will store the screen object
# turtle.Screen instantiates a screen object

# data types that are objects normally have a behavior attached
# behaviors are functions or methods
# Create a screen and a turtle object
screen = turtle.Screen()
screen.title("Turtle Example in Python")

# create a turtle instance - you are instantiating a turtle object
my_turtle = turtle.Turtle()

# Draw a square
# the 'for' loop will loop through the same code 4x
# the i represents the loop variable
i=0
for i in range(4):
    print(i)
    my_turtle.forward(100)  # Move forward by 100 units
    my_turtle.right(90)     # Turn right by 90 degrees

# Keep the window open until clicked
closeWindow = input("Press any key to close window. ")
screen.mainloop()

# Keep the window open until clicked
turtle.done()