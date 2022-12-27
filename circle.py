import turtle

# Create a turtle object and set its speed to the maximum value
t = turtle.Turtle()
t.speed(0)

# Define a function to draw a circle and rotate the turtle
def draw_circle(angle):
    t.circle(100)
    t.left(angle)

# Use a for loop to draw the circle and rotate the turtle at each frame
for i in range(360):
    draw_circle(1)

# Keep the window open until it is closed by the user
turtle.mainloop()
