# =========================================================
# N-Queens Problem using Backtracking
# =========================================================

backtrack_count = 0
solutions = []


# ---------------------------------------------------------
# Check whether a queen can be placed safely
# ---------------------------------------------------------

def is_safe(board, row, col):

    for prev_row in range(row):

        placed = board[prev_row]

        # Same column
        if placed == col:
            return False

        # Same diagonal
        if abs(placed - col) == abs(prev_row - row):
            return False

    return True


# ---------------------------------------------------------
# Backtracking function
# ---------------------------------------------------------

def solve_n_queens(board, row, n):

    global backtrack_count

    # All queens placed
    if row == n:
        solutions.append(board[:])
        return

    found = False

    for col in range(n):

        if is_safe(board, row, col):

            found = True

            board[row] = col

            solve_n_queens(board, row + 1, n)

            # Backtrack
            board[row] = -1
            backtrack_count += 1

    return


# ---------------------------------------------------------
# Solve N-Queens
# ---------------------------------------------------------

def n_queens(n):

    global backtrack_count
    global solutions

    backtrack_count = 0
    solutions = []

    board = [-1] * n

    solve_n_queens(board, 0, n)

    return solutions, backtrack_count


# ---------------------------------------------------------
# Print Chess Board
# ---------------------------------------------------------

def print_board(solution):

    n = len(solution)

    border = "+" + "---+" * n

    print(border)

    for row in range(n):

        print("|", end="")

        for col in range(n):

            if solution[row] == col:
                print(" Q |", end="")
            else:
                print(" . |", end="")

        print()
        print(border)


# =========================================================
# N = 4, 6 and 8
# =========================================================

for n in [4, 6, 8]:

    sols, backs = n_queens(n)

    print(f"N={n}: {len(sols)} solutions, {backs} backtracks")


# =========================================================
# Display all solutions for 4-Queens
# =========================================================

sols, backs = n_queens(4)

print("\nAll solutions for 4-Queens:")

for i, solution in enumerate(sols, 1):

    print(f"Solution {i}: {solution}")

    print_board(solution)