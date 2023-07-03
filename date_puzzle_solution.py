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

pieces = [
    [[1, 1],
     [1, 0],
     [1, 1]],

    [[1, 0],
     [1, 1],
     [1, 0],
     [1, 0]],

    [[1, 1],
     [1, 0],
     [1, 0],
     [1, 0]],

    [[1, 1, 1],
     [1, 0, 0],
     [1, 0, 0]],

    [[1, 1],
     [1, 1],
     [1, 1]],

    [[1, 0],
     [1, 1],
     [1, 1]],

    [[1, 0],
     [1, 1],
     [0, 1],
     [0, 1]],

    [[1, 1, 0],
     [0, 1, 0],
     [0, 1, 1]]]

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


# TODO
def placeable(start, piece, curr_board):
    placed = False

    # TODO
    def attempt_placement(attempt_piece):
        return False

    # try all (of 4) rotations, transpose and try each rotation again
    for i in range(8):
        # try it
        if attempt_placement(piece):
            continue

        # if it failed, rotate unless time to transpose
        if i == 3:
            piece = [[piece[j][i] for j in range(len(piece))] for i in range(len(piece[0]))]
        else:
            piece = [[piece[j][i] for j in range(len(piece))] for i in range(len(piece[0]) - 1, -1, -1)]


# Place a specified piece on the board (checking whether it should be done *should* be checked beforehand)
def place_piece(start, piece, curr_board):
    new_board = curr_board.copy()

    # place a new piece on the board for every location the piece would be present
    for idx, i in enumerate(piece):
        for jdx, j in enumerate(i):
            if j == 1:
                new_board[start[0] + idx][start[1] + jdx] = 1

    return new_board


# Find the position closest to the top and the left that isn't yet marked
def start_pos(curr_board):

    # iterate through and return the first position that isn't marked
    for idx, i in enumerate(curr_board):
        for jdx, j in enumerate(i):
            if j == 0:
                return idx, jdx


def solve_board(curr_board, curr_pieces):

    print(curr_board)

    start = start_pos(curr_board)

    print(start)

    new_board = place_piece(start, curr_pieces[0], curr_board)

    print(new_board)


    # for idx, piece in enumerate(curr_pieces):
    #     if placeable(start, piece, curr_board):
    #
    #         # remove piece from curr_pieces to recurse on
    #         new_pieces = curr_pieces
    #         del new_pieces[idx]
    #
    #         # if this was the last piece then just return
    #         if len(new_pieces) == 0:
    #             return
    #         else:
    #             # create a board with the piece placed down
    #             new_board = place_piece(start, piece, curr_board)
    #
    #             # recurse and see if it is successful
    #             sol = solve_board(new_board, new_pieces)
    #
    #             if sol[0]:  # sol[0] is a boolean representing success
    #                 return [start, piece] + sol[1]  # sol[1] is the solution found on the recursion

    # return a list of tuples (start pos, order of directions)
    return


solve_board(solvable_board, pieces)

# ----------------------------------------------- Print the solution! --------------------------------------------------


print("You asked for the solution for the date '" + input_month + " " + str(input_day) + "'. Here is the solution!")

# Creating a turtle object(pen)
# pen = turtle.Turtle()


# Defining method to draw a colored circle
# with a dynamic radius
# def ring(col, rad):
#     # Set the fill
#     pen.fillcolor(col)
#
#     # Start filling the color
#     pen.begin_fill()
#
#     # Draw a circle
#     pen.circle(rad)
#
#     # Ending the filling of the color
#     pen.end_fill()


##########################Main Section#############################

# pen.up             --> move turtle to air
# pen.down           --> move turtle to ground
# pen.setpos         --> move turtle to given position
# ring(color, radius) --> draw a ring of specified color and radius
###################################################################

# Draw ears
# pen.up()
# pen.setpos(-35, 95)
# pen.down()
# ring("red", 25)
# pen.hideturtle()
