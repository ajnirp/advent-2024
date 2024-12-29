# Running with python: use open(0)
# Command: python3 6.py < 6.txt
# time python3 6.py < 6.txt
# real  0m48.055s
# user    0m47.999s
# sys 0m0.056s

# Running with pypy: replace open(0) with open('6.txt', 'r')
# Command: time pypy 6.py
# real    0m10.647s
# user    0m10.570s
# sys 0m0.057s

from util import *

with open(0) as file:
    grid = file.read().strip().split('\n')
    grid = [[c for c in row] for row in grid]

def TurnRight(direction): return (direction + 1) % 4

def FindStart(grid):
    for r in range(NumRows(grid)):
        for c in range(NumCols(grid)):
            if grid[r][c] == '^':
                return r, c


# Returns a list of cells visited if the guard can exit the grid. Returns None
# if there is a loop in the grid.
def Traverse(grid):
    DIRECTION_VECTORS = [(-1,0), (0,1), (1,0), (0,-1)]
    num_rows = NumRows(grid)
    num_cols = NumCols(grid)
    r, c = FindStart(grid)
    moves = set()
    direction = 0  # 0 N, 1 E, 2 S, 3 W
    while True:
        if (r, c, direction) in moves:
            return None
        moves.add((r, c, direction))
        dr, dc = DIRECTION_VECTORS[direction]
        next_r, next_c = r + dr, c + dc
        if not (IsInBounds(next_r, num_rows) and IsInBounds(next_c, num_cols)):
            break
        if grid[next_r][next_c] == '#':
            direction = TurnRight(direction)
            continue
        r, c = next_r, next_c
    cells_visited = set((r, c) for r, c, _ in moves)
    return cells_visited

def Part1(grid):
    return len(Traverse(grid))

# Replace every visited cell with an obstacle and rerun the search.
def Part2(grid):
    result = 0
    start_r, start_c = FindStart(grid)
    cells_visited = Traverse(grid)
    for r, c in cells_visited:
        if (r, c) == (start_r, start_c):
            continue
        grid[r][c] = '#'
        traversal = Traverse(grid)
        if not traversal:
            result += 1
        grid[r][c] = '.'
    return result

print(Part1(grid))  # 4890
print(Part2(grid))  # 1995
