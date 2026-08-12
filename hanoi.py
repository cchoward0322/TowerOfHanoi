# hanoi.py is a recursive Tower of Hanoi solver
# pm() and hanoi() are both copied from TowerOfHanoi.ipynb
# python cannot import from a .ipynb file so this .py file is for visualizer.py to use them

# only change is now the pm records each move in moves

#turning moves into data as (start, end) pair
# recording pm
moves = []

def pm(start, end):
    print(f"Move disk from {start} to {end}")
    moves.append((start, end)) #record every move so visualizer can play later

#clear pegs each call so it doesn't keep adding to moves
def solve(n, start, end, num_pegs=3):
    moves.clear()
    hanoi(n, start, end, num_pegs)
    return moves


def hanoi(n, start, end, num_pegs=3):
    if n == 1: #run UI with only one disk
        pm(start, end)  #move the single disk directly from start to end
    else:
        # Find an auxiliary peg (any peg that is not start or end)
        temp = None
        for peg in range(1, num_pegs + 1):
            if peg != start and peg != end:
                temp = peg
                break
        
        hanoi(n - 1, start, temp, num_pegs)  #move n-1 disks from start to temp
        pm(start, end)  #move the largest disk from start to end
        hanoi(n - 1, temp, end, num_pegs)  #move n-1 disks from temp to end


# needed so we did not loop
if __name__ == "__main__":
    answer = solve(3, 1, 3, num_pegs=3)
    print(answer)