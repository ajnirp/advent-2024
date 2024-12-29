from util import *

with open(0) as file:
    grid = [line.strip() for line in file.readlines()]

# Returns a pair of lists. The first is a list of horizontal walls, represented
# by their left ends. The second is a list of vertical walls, represented by
# their top ends. The perimeter can be obtained as a sum of the lengths of these
# two lists.

# A horizontal wall is represented as (rr, cc, sign) where `(rr, cc)` are the
# coordinates of its *left* end, and `sign` is +1 if the region is above the
# wall and -1 if the region is below the wall.

# A vertical wall is represented as (rr, cc, sign) where `(rr, cc)` are the
# coordinates of its *top* end, and `sign` is +1 if the region is to the left of
# the wall and -1 if the region is to the right of the wall.

# The numbering is as follows: `0` represents all horizontal walls to
# top of row `0`. `kNumRows` represents all horizontal walls to the bottom of
# row `kNumRows - 1`. Likewise for vertical walls, which run from `0` to
# `kNumCols`, both inclusive.

# In this function, the parameters `(r, c)` represent a cell *inside* the
# region whose walls we're accumulating.
def AccumulateWalls(r, c, grid, num_rows, num_cols, horizontal_walls, vertical_walls):
    for nr, nc in Neighbors(r, c):
        if not IsInGrid(nr, num_rows, nc, num_cols) or grid[nr][nc] != grid[r][c]:
            if nr == r:
                if c > nc: vertical_walls.append((r, c, 1))
                else: vertical_walls.append((r, nc, -1))
            if nc == c:
                if r > nr: horizontal_walls.append((r, c, -1))
                else: horizontal_walls.append((nr, c, 1))
    return horizontal_walls, vertical_walls

# Given a starting cell `(r, c)`, computes the area of its connected component
# and also a list of the component's horizontal and vertical walls.
def ComputeAreaAndWalls(r, c, grid, seen):
    kNumRows, kNumCols = NumRows(grid), NumCols(grid)
    kStartValue = grid[r][c]
    queue = [(r, c)]
    horizontal_walls, vertical_walls = [], []
    area = 0
    while queue:
        next_wave = []
        for (rr, cc) in queue:
            if seen[rr][cc]: continue
            seen[rr][cc] = True
            area += 1
            AccumulateWalls(rr, cc, grid, kNumRows, kNumCols, horizontal_walls, vertical_walls)
            for nr, nc in ValidNeighbors(rr, cc, kNumRows, kNumCols):
                if grid[nr][nc] != kStartValue: continue
                next_wave.append((nr, nc))
        queue = next_wave
    return area, horizontal_walls, vertical_walls

# Computes the number of sides of a connected component given a list of
# horizontal walls and a list of its vertical walls.
# The `else: result += next_sign != prev_sign` lines account for the edge case
# mentioned in the question (copied to file `12t2.txt`), in which what looks
# a single continuous fence is actually two parts with opposite orientations.
def ComputeNumberOfSides(horizontal_walls, vertical_walls):
    horizontal_walls.sort()
    result = 1
    for i in range(1, len(horizontal_walls)):
        next_r, next_c, next_sign = horizontal_walls[i]
        prev_r, prev_c, prev_sign = horizontal_walls[i-1]
        if next_r != prev_r or next_c != prev_c + 1: result += 1
        else: result += next_sign != prev_sign
    result += 1
    vertical_walls.sort(key=lambda pair: (pair[1], pair[0]))
    for i in range(1, len(vertical_walls)):
        next_r, next_c, next_sign = vertical_walls[i]
        prev_r, prev_c, prev_sign = vertical_walls[i-1]
        if next_c != prev_c or next_r != prev_r + 1: result += 1
        else: result += next_sign != prev_sign
    return result

def TotalFencingPrice(grid):
    kNumRows, kNumCols = NumRows(grid), NumCols(grid)
    seen = [[False for _ in range(kNumCols)] for _ in range(kNumRows)]
    part_1, part_2 = 0, 0
    for r in range(kNumRows):
        for c in range(kNumCols):
            if seen[r][c]: continue
            area, horizontal_walls, vertical_walls = ComputeAreaAndWalls(r, c, grid, seen)
            perimeter = len(horizontal_walls) + len(vertical_walls)
            num_sides = ComputeNumberOfSides(horizontal_walls, vertical_walls)
            part_1 += area * perimeter
            part_2 += area * num_sides
    return part_1, part_2

print(TotalFencingPrice(grid))  # (1457298, 921636)
