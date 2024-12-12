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


with open(0) as file:
    grid = file.read().strip().split('\n')
    grid = [[c for c in row] for row in grid]

def NumRows(grid): return len(grid)
def NumCols(grid): return len(grid[0])  # Assumes `grid` is not empty.
def IsInBounds(idx, max_idx): return 0 <= idx < max_idx
def TurnRight(direction): return (direction + 1) % 4

def FindStart(grid):
    for r in range(NumRows(grid)):
        for c in range(NumCols(grid)):
            if grid[r][c] == '^':
                return r, c

DIRECTION_VECTORS = [(-1,0), (0,1), (1,0), (0,-1)]

def Traverse(grid, start_r, start_c, start_direction, unique_moves):
    global DIRECTION_VECTORS
    kNumRows = NumRows(grid)
    kNumCols = NumCols(grid)
    r, c = start_r, start_c
    direction = start_direction  # 0 N, 1 E, 2 S, 3 W
    all_moves = []
    while True:
        if (r, c, direction) in unique_moves:
            return None
        move = (r, c, direction)
        unique_moves.add(move)
        all_moves.append(move)
        dr, dc = DIRECTION_VECTORS[direction]
        next_r, next_c = r + dr, c + dc
        if not (IsInBounds(next_r, kNumRows) and IsInBounds(next_c, kNumCols)):
            break
        if grid[next_r][next_c] == '#':
            direction = TurnRight(direction)
            continue
        r, c = next_r, next_c
    return all_moves

def Part1(grid):
    kStartRow, kStartCol = FindStart(grid)
    unique_moves = set()
    all_moves = Traverse(grid, kStartRow, kStartCol, 0, unique_moves)
    cells_visited = set((r, c) for r, c, _ in all_moves)
    return len(cells_visited)

# Replace every visited cell with an obstacle and rerun the search.
def Part2(grid):
    result = 0
    kStartRow, kStartCol = FindStart(grid)
    kNumRows = NumRows(grid)
    kNumCols = NumCols(grid)
    unique_moves = set()
    all_moves = Traverse(grid, kStartRow, kStartCol, 0, unique_moves)
    for idx in range(1, len(all_moves)):
        r, c, direction = all_moves[idx - 1]  # previous move
        if (r, c) == (kStartRow, kStartCol) and direction == 0:
            continue
        grid_copy = [[c for c in row] for row in grid]
        grid_copy[r][c] = '#'
        moves_prefix = set(all_moves[:idx])
        traversal = Traverse(grid_copy, r, c, direction, moves_prefix)
        if not traversal:
            result += 1
    return result

print(Part1(grid))
print(Part2(grid))
