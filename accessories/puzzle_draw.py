import turtle

# Creating a turtle object(pen)
pen = turtle.Turtle()


# Defining method to draw a colored circle
# with a dynamic radius
def ring(col, rad):
    # Set the fill
    pen.fillcolor(col)

    # Start filling the color
    pen.begin_fill()

    # Draw a circle
    pen.circle(rad)

    # Ending the filling of the color
    pen.end_fill()


#########################Main Section#############################

# pen.up             --> move turtle to air
# pen.down           --> move turtle to ground
# pen.setpos         --> move turtle to given position
# ring(color, radius) --> draw a ring of specified color and radius
##################################################################

# Draw ears
pen.up()
pen.setpos(-35, 95)
pen.down()
ring("red", 25)
pen.hideturtle()