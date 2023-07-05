# TITLE: A file to house all functions that help to run accessories.puzzle_solution.solve_board()

import copy

# ------------------------------------------- Set Board ------------------------------------------------


def set_board(board, month="NOT SET", day=-99):
    solvable_board = [[0 for i in j] for j in board]

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

    return solvable_board


# ------------------------------------------- Placeable ------------------------------------------------


def placeable(start, piece, curr_board):
    # check for each part of the piece that there is not overlap
    for idx, elem in enumerate(piece):

        # if the row would be out of range
        if (start[0] + idx) > len(curr_board) - 1:
            return False

        for jdx, j in enumerate(elem):

            # only matters if the piece would actually occupy that space (aka the value is 1)
            if j == 1:

                # if the col would be out of range for that given row
                if (start[1] + jdx) > len(curr_board[start[0] + idx]) - 1:
                    return False

                if curr_board[start[0] + idx][start[1] + jdx] == 1:
                    return False

    # check if it would create a bad spot
    # TODO: this would probably speed things up a bit, but currently not accurate, sometimes things aren't necessarily
    #  bad spots, they may be filled later (by a piece starting on its left)
    # temp_board = place_piece(start, piece, curr_board)
    # for i in range(start[0], start[0] + len(piece)):  # for each row that the piece would occupy
    #     for jdx, j in enumerate(temp_board[i]):
    #         if jdx < start[1] + len(piece[0]) + 1:  # only check parts of board just to right of rightmost part of
    #         # piece
    #
    #             # if the spot is not occupied, check if it is a dead spot
    #             if j == 0:
    #                 if bad_start((i, jdx), temp_board):
    #                     return False

    return True


# ------------------------------------------- Place Piece ------------------------------------------------

# Place a specified piece on the board (the checking of whether it can be done *should've* been checked beforehand)
def place_piece(start, piece, curr_board):
    new_board = copy.deepcopy(curr_board)

    # place a new piece on the board for every location the piece would be present
    for idx, i in enumerate(piece):
        for jdx, j in enumerate(i):
            if j == 1:
                new_board[start[0] + idx][start[1] + jdx] = 1

    return new_board


# ------------------------------------------- Start Pos ------------------------------------------------


# Find the position closest to the top and the left that isn't yet marked
def start_pos(curr_board):
    # iterate through and return the first position that isn't marked
    for idx, i in enumerate(curr_board):
        for jdx, j in enumerate(i):
            if j == 0:
                return idx, jdx


# ------------------------------------------- Bad Start ------------------------------------------------


# note: this is assuming it has been chosen as a start pos (not spaces above or to the left of it
def bad_start(start, curr_board):
    # note: there is no way that the start can be at the bottom of the board, so this does not need to be checked
    # if the below spot is occupied

    if start[0] == 6:
        # raise ValueError("There is no solution in which a piece's top right part starts on row index 6. There is a "
        #                  "problem!")
        return True
    # TODO THIS IS A TEMP FIX

    if start[0] == 5 and start[1] > 2:  # if there is no space below us don't run the next if (out of bounds)

        # if no space on board to the right
        if start[1] == len(curr_board[start[0]]) - 1:
            return True

        # if the right spot is occupied
        elif curr_board[5][start[1] + 1] == 1:
            return True

    elif curr_board[start[0] + 1][start[1]] == 1:

        # if no space on board to the right
        if start[1] == len(curr_board[start[0]]) - 1:
            return True

        # if the right spot is occupied
        elif curr_board[start[0]][start[1] + 1] == 1:
            return True

    # otherwise, it may not be a bad start
    return False

