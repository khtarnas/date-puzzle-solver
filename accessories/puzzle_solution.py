import copy
from accessories.puzzle_solution_helpers import set_board, placeable, place_piece, start_pos, bad_start


def solve_board(board, pieces, month, day):
    solvable_board = set_board(board, month, day)
    solution = solve_board_recurse(solvable_board, pieces, 0)
    if solution[0]:
        return solution[1]
    else:
        return "ERROR: SOLUTION UNABLE TO BE FOUND"


def solve_board_recurse(curr_board, curr_pieces, depth):  # TODO: depth is only used for debugging

    # Get the start position
    start = start_pos(curr_board)
    start_row = start[0]
    start_col = start[1]
    if bad_start(start, curr_board):  # TODO: this should likely be useless if the checking
                                      #  in placeable is effective --- NOT RN THO!!! very useful
        return False, None

    # iterate through all possible pieces that could be placed
    for idx, piece in enumerate(curr_pieces):
        if idx > 0 and depth == 0:
            continue

        # remove piece from curr_pieces for recursion
        # note: this will only impact our iteration focused on this piece
        new_pieces = copy.deepcopy(curr_pieces)
        del new_pieces[idx]

        # try all (of 4) rotations, transpose and try each rotation again (recursing for each rotation)
        for i in range(8):

            # TODO DEBUGGING STUFF REMOVE
            if piece == [[0, 1, 1], [0, 1, 0], [1, 1, 0]] and depth == 4:
                print("hi")

            # if the piece only fits given moving the start position out of bounds, then continue to the next
            if start_col >= 0:
                if placeable((start_row, start_col), piece, curr_board):
                    # print("placeable!")

                    # if this was the last piece then just return
                    if len(new_pieces) == 0:
                        return True, []
                    else:
                        # create a board with the piece placed down
                        new_board = place_piece((start_row, start_col), piece, curr_board)

                        # recurse and see if it is successful
                        sol = solve_board_recurse(new_board, new_pieces, depth + 1)

                        if sol[0]:  # sol[0] is a boolean representing success
                            print("SUCCESSFUL!")
                            print(sol[1])

                            # sol[1] is the solution found on the recursion
                            return True, [(start_row, start_col), piece] + sol[1]

                        # else, just continue on to the next attempt

            # if it failed, rotate unless time to transpose
            if i == 3:
                piece = [[piece[j][i] for j in range(len(piece))] for i in range(len(piece[0]))]
            else:
                piece = [[piece[j][i] for j in range(len(piece))] for i in range(len(piece[0]) - 1, -1, -1)]

            # move the start position to the left until the left most 1 on the top row of the piece is at the start pos
            # this will move the start position to be negative at times, we will skip that above
                # TODO: this can probably be cleaned up
                if piece[0][0] == 0:
                    if piece[0][1] == 0:
                        if piece[0][2] == 0:
                            start_col = start_pos(curr_board)[1] - 3
                        else:
                            start_col = start_pos(curr_board)[1] - 2
                    else:
                        start_col = start_pos(curr_board)[1] - 1
                else:
                    start_col = start_pos(curr_board)[1]

    # If we reach this point, there was no solution found
    # note: this should NOT happen on the top layer, but SHOULD happen on lower levels
    return False, None
