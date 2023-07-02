import sys
import turtle

# ------------------------------------------- Set the initial variables ------------------------------------------------


board = [["jan", "feb", "mar", "apr", "may", "june"],
         ["july", "aug", "sep", "oct", "nov", "dec"],
         [1, 2, 3, 4, 5, 6, 7],
         [8, 9, 10, 11, 12, 13, 14],
         [15, 16, 17, 18, 19, 20, 21],
         [22, 23, 24, 25, 26, 27, 29],
         [29, 30, 31]
         ]

solvable_board = [[0 for i in j] for j in board]

# this may be easier to be done as a 3 x 3 matrix with 1s for yes and 0s for nos
pieces = [["right", "down", "down", "right"],
          ["right", "down", "down", "down"],
          ["right", "down", "left", "down", "right"],
          ["down", "right", "down", "down"],
          ["right", "right", "down", "down"],
          ["down", "down", "right", "left", "down"],  # this one is a bit difficult because it overlaps itself...
          ["down", "right", "down", "left"],
          ["right", "down", "down", "left"]]

# take command-line args
input_month = sys.argv[1]
input_day = int(sys.argv[2])


# ------------------ Set the initial state of the board (occupy the spaces that cannot be filled) ----------------------


def set_board(month="NOT SET", day=-99):
    # set month (only if not set yet)
    month_set = False
    for idx, x in enumerate(board[0]):
        if x == month:
            solvable_board[0][idx] = 1
            month_set = True

    if not month_set:
        for idx, x in enumerate(board[1]):
            if x == month:
                solvable_board[1][idx] = 1
                month_set = True

    # throw error if month value did not match anything
    if not month_set:
        print("Month not properly set; you set month as '" + month +
              "'. Please set month as the first three letters of the month you want to indicate.")
        raise ValueError("Month not properly set; you set month as '" + month +
                         "'. Please set month as the first three letters of the month you want to indicate.")

    # set day
    day -= 1
    row = (day // 7) + 2
    col = day % 7

    try:
        solvable_board[row][col] = 1
    except:

        # throw error if the value wasn't a reasonable one
        if day == -99:
            day = "NOT SET"
        print("Day not properly set; you set day as " + str(day) +
              ". Please set day as an integer between 1 and 31 (inclusive)")
        raise ValueError("Day not properly set; you set day as " + str(day) +
                         ". Please set day as an integer between 1 and 31 (inclusive)")


set_board(input_month, input_day)


# ------------------------------------------- Solve the board! ---------------------------------------------------------


def solve_board():
    print(solvable_board)


# rotate each piece all four possible ways

# I need to make sure to NOT add the pieces to the completed board until after so that the overlapping piece doesn't
# infinite fail

solve_board()

# ----------------------------------------------- Print the solution! --------------------------------------------------


print("You asked for the solution for the date '" + input_month + " " + str(input_day) + "'. Here is the solution!")


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


##########################Main Section#############################

# pen.up             --> move turtle to air
# pen.down           --> move turtle to ground
# pen.setpos         --> move turtle to given position
# ring(color, radius) --> draw a ring of specified color and radius
###################################################################

# Draw ears
pen.up()
pen.setpos(-35, 95)
pen.down()
ring("red", 25)
pen.hideturtle()
