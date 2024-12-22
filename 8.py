# python3 8.py < 8.txt

from collections import defaultdict
from util import *

with open(0) as file:
    grid = [line.strip() for line in file.readlines()]

def FindAntennaLocations(grid):
    antenna_locations = defaultdict(list)
    kNumRows, kNumCols = NumRows(grid), NumCols(grid)
    for row in range(kNumRows):
        for col in  range(kNumCols):
            if grid[row][col] != '.':
                antenna_locations[grid[row][col]].append((row, col))
    return antenna_locations

# For a given pair of antennas, generate all antinodes for them. For part 1,
# this only generates two antinodes at most. For part 2, this generates as many
# antinodes in either direction as can fit into the grid.
def GenerateAntinodes(r1, c1, r2, c2, part_2, num_rows, num_cols):
    if (r1, c1) == (r2, c2):
        raise ValueError("The antennas coincide")
    temp = []
    # Put r1, c1 on top
    if r1 <= r2:
        r1, c1, r2, c2 = r2, c2, r1, c1
    row_diff = r2 - r1
    col_diff = c2 - c1
    # r1, c1 => r2, c2 goes down and right
    if c1 < c2:
        rleft, cleft = r1 - row_diff, c1 - col_diff
        rright, cright = r2 + row_diff, c2 + col_diff
        temp.append((rleft, cleft))
        temp.append((rright, cright))
    # r1, c1 => r2, c2 goes down and left
    else:
        col_diff = -col_diff
        rleft, cleft = r2 + row_diff, c2 - col_diff
        rright, cright = r1 - row_diff, c1 + col_diff
        temp.append((rleft, cleft))
        temp.append((rright, cright))
    result = []
    for (r, c) in temp:
        if IsInBounds(r, num_rows) and IsInBounds(c, num_cols):
            result.append((r, c))
    return result


# Find all antinodes for all antennas.
def FindAllAntinodes(antenna_locations, part_2, num_rows, num_cols):
    result = set()
    for antenna, locations in antenna_locations.items():
        if len(locations) < 2:
            continue
        for i in range(len(locations)):
            for j in range(i + 1, len(locations)):
                r1, c1 = locations[i]
                r2, c2 = locations[j]
                antinodes = GenerateAntinodes(r1, c1, r2, c2, part_2, num_rows, num_cols)
                for antinode in antinodes:
                    result.add(antinode)
    return result

def Solve(grid, part_2):
    antenna_locations = FindAntennaLocations(grid)
    kNumRows, kNumCols = NumRows(grid), NumCols(grid)
    all_antinodes = FindAllAntinodes(antenna_locations, part_2, kNumRows, kNumCols)
    if part_2:
        for _, location in antenna_locations:
            all_antinodes.add(location)
    return len(all_antinodes)

# Part 1
print(Solve(grid, False))

# Part 2
# print(Solve(grid, True))