from puzzle_helpers import set_board, placeable, place_piece, start_pos, bad_start


def solve_board(board, pieces, month, day):
    solvable_board = set_board(board, month, day)
    solve_board_recurse(solvable_board, pieces, 0)


def solve_board_recurse(curr_board, curr_pieces, depth):  # TODO: depth is only used for debugging
    # print(depth)
    # print(curr_board)
    # print(curr_pieces)

    # print(curr_board)

    start = start_pos(curr_board)
    if bad_start(start, curr_board):
        return False, None

    # print(start)
    #
    # print(placeable(start, curr_pieces[0], curr_board))
    #
    # new_board = place_piece(start, curr_pieces[0], curr_board)
    #
    # print(new_board)
    #
    # print(placeable(start, curr_pieces[0], curr_board))

    for idx, piece in enumerate(curr_pieces):
        if idx > 0 and depth == 0:
            continue

        # print("We are on piece number " + str(idx + 1))
        # print(piece)

        # remove piece from curr_pieces to recurse on
        # note: this will only impact our iteration focused on this piece
        new_pieces = copy.deepcopy(curr_pieces)
        del new_pieces[idx]

        # # try all (of 4) rotations, transpose and try each rotation again (recursing for each rotation)
        for i in range(8):
            # print(idx)
            # print(i)
            # print(curr_pieces)
            if placeable(start, piece, curr_board):
                # print("placeable!")

                # if this was the last piece then just return
                if len(new_pieces) == 0:
                    return True, []
                else:
                    # create a board with the piece placed down
                    new_board = place_piece(start, piece, curr_board)

                    # recurse and see if it is successful
                    # print("recursing...")
                    sol = solve_board(new_board, new_pieces, depth + 1)

                    # print(sol)
                    if sol[0]:  # sol[0] is a boolean representing success
                        "SUCCESSFUL!"
                        return [start, piece] + sol[1]  # sol[1] is the solution found on the recursion

                    # else, just continue on to the next attempt

            # if it failed, rotate unless time to transpose
            if i == 3:
                piece = [[piece[j][i] for j in range(len(piece))] for i in range(len(piece[0]))]
            else:
                piece = [[piece[j][i] for j in range(len(piece))] for i in range(len(piece[0]) - 1, -1, -1)]

            # print(idx)

        # print(curr_pieces)

    # If we reach this point, there was no solution found
    # note: this should NOT happen on the top layer, but SHOULD happen on lower levels
    return False, None
