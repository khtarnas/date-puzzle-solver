import copy
from accessories.puzzle_solution_helpers import set_board, placeable, place_piece, start_pos, bad_start


def solve_board(board, pieces, month, day):
    solvable_board = set_board(board, month, day)
    solve_board_recurse(solvable_board, pieces, 0)


def solve_board_recurse(curr_board, curr_pieces, depth):  # TODO: depth is only used for debugging

    # Get the start position
    start = start_pos(curr_board)
    start_x = start[0]
    start_y = start[1]
    if bad_start(start, curr_board):  # TODO: this should likely be useless if the checking in placeable is effective
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
            start_pos_moved = False  # a variable to represent whether the start pos was moved because of a rotation

            if piece == [[1, 1], [0, 1], [0, 1], [0, 1]]:
                print("we be here!")
                print(depth)

            if placeable((start_x, start_y), piece, curr_board):
                # print("placeable!")

                # if this was the last piece then just return
                if len(new_pieces) == 0:
                    return True, []
                else:
                    # create a board with the piece placed down
                    new_board = place_piece((start_x, start_y), piece, curr_board)

                    # recurse and see if it is successful
                    sol = solve_board_recurse(new_board, new_pieces, depth + 1)

                    # print(sol)
                    if sol[0]:  # sol[0] is a boolean representing success
                        print("SUCCESSFUL!")
                        return [(start_x, start_y), piece] + sol[1]  # sol[1] is the solution found on the recursion

                    # else, just continue on to the next attempt

            # if it failed, rotate unless time to transpose
            if i == 3:
                piece = [[piece[j][i] for j in range(len(piece))] for i in range(len(piece[0]))]
            else:
                piece = [[piece[j][i] for j in range(len(piece))] for i in range(len(piece[0]) - 1, -1, -1)]

            # only do this if we aren't at the far left
            if start_pos(curr_board)[0] != 0:

                # if the top left part of the piece is empty then move it
                if piece[0][0] == 0:
                    start_x = start_pos(curr_board)[0] - 1
                else:
                    start_x = start_pos(curr_board)[0]

    # If we reach this point, there was no solution found
    # note: this should NOT happen on the top layer, but SHOULD happen on lower levels
    return False, None
