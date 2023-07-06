import sys
from accessories import puzzle_settings
from accessories.puzzle_solution import solve_board

# Retrieve board settings
pieces = puzzle_settings.pieces
board = puzzle_settings.board

# take command-line args
# month = sys.argv[1]
# day = int(sys.argv[2])

# TODO: temp/testing
month = "jul"
day = 6


# call the solution function from accessories.puzzle_solution.py
solution = solve_board(board, pieces, month, day)
print(solution)


print("You asked for the solution for the date '" + month
      + " " + str(day) + "'. Here is the solution: \n")

for i in solution:
    print(i)
    # print(str(i[1]) + " starts at position " + str(i[0]))
