from bisect import bisect_left
from copy import deepcopy
from util import *

with open(0) as file:
    coords = [tuple(map(int, line.strip().split(','))) for line in file.readlines()]

WIDTH, HEIGHT = 71, 71

grid = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]

def DropByte(index, grid, coords):
    x, y = coords[index]
    grid[y][x] += 1

def Bfs(start, goal, grid):
    start_r, start_c = start
    goal_r, goal_c = goal
    if grid[goal_r][goal_c] > 0 or grid[start_r][start_c] > 0:
        return -1
    num_rows, num_cols = NumRows(grid), NumCols(grid)
    queue = [(start_r, start_c, 0)]
    seen = set()
    while queue:
        next_wave = []
        for r, c, dist in queue:
            for nr, nc in ValidNeighbors(r, c, num_rows, num_cols):
                if grid[nr][nc] > 0: continue  # obstacle
                if (nr, nc) in seen: continue
                if (nr, nc) == goal: return dist + 1
                next_wave.append((nr, nc, dist + 1))
                seen.add((nr, nc))
        queue = next_wave
    return -1  # goal not found

def Part1(grid, coords):
    grid_copy = deepcopy(grid)
    for index in range(1024):
        DropByte(index, grid_copy, coords)
    return Bfs((0, 0), (HEIGHT-1, WIDTH-1), grid_copy)

# Naive implementation.
def Part2(grid, coords):
    grid_copy = deepcopy(grid)
    for index in range(len(coords)):
        DropByte(index, grid_copy, coords)
        if Bfs((0, 0), (HEIGHT-1, WIDTH-1), grid_copy) == -1:
            return coords[index]
        
# Binary search implementation. ~4x faster than naive.
def Part2BinarySearch(grid, coords):
    def SortKey(grid):
        return 1 if Bfs((0, 0), (HEIGHT-1, WIDTH-1), grid) == -1 else 0
    grids = [deepcopy(grid)]
    for index in range(len(coords)):
        next_grid_copy = deepcopy(grids[-1])
        DropByte(index, next_grid_copy, coords)
        grids.append(next_grid_copy)
    index = bisect_left(grids, 1, key=SortKey) - 1
    return coords[index]

print(Part1(grid, coords))  # 268
print(Part2BinarySearch(grid, coords))  # (64, 11)