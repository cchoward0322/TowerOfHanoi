# hanoi.py is a recursive Tower of Hanoi solver
# pm() and hanoi() are both copied from TowerOfHanoi.ipynb
# python cannot import from a .ipynb file so this .py file is for visualizer.py to use them

# only change is now the pm records each move in moves

# Turning moves into data as (start, end) pair
# recording pm
moves = []

# Moved the pm func above def hanoi for syntax
def pm(start, end):
    print(f"Move disk from {start} to {end}")
    moves.append((start, end)) # record so UI can play later

# Needs to be cleared before so it does not stack if solve is called twice
def solve(n, start, end):
    moves.clear()
    hanoi(n, start, end)
    return moves


def hanoi(n, start, end):
    if n == 1:
        pm(start, end)  # Move the single disk directly from start to end
    else:
        temp = 6 - start - end  # Calculate the temporary peg (assuming pegs are numbered 1, 2, 3), 6 represents the sum of the peg numbers (1 + 2 + 3)
        hanoi(n - 1, start, temp)  # Move n-1 disks from start to temp
        pm(start, end)  # pm stands for print moves, which prints the move of the nth disk from start to end
        hanoi(n - 1, temp, end)  # Move the n-1 disks from temp to end


# needed so we did not loop
if __name__ == "__main__":
    answer = solve(3, 1, 3)
    print(answer)