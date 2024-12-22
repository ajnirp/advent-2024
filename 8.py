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
    if r1 <= r2:
        r1, c1, r2, c2 = r2, c2, r1, c1  # Put r1, c1 on top.
    abs_row_diff, abs_col_diff = r2 - r1, abs(c2 - c1)  # Both +ve.
    direction_vectors = [(-1, -1), (1, 1)] if c1 < c2 else [(-1, 1), (1, -1)]
    starts = [(r1, c1), (r2, c2)]
    for (dr, dc), (r, c) in zip(direction_vectors, starts):
        dr *= abs_row_diff
        dc *= abs_col_diff
        while True:
            r += dr
            c += dc
            if not (IsInBounds(r, num_rows) and IsInBounds(c, num_cols)): break
            yield (r, c)
            if not part_2: break  # For part 1, break after just one iteration.

# Find all antinodes for all antennas.
def FindAllAntinodes(antenna_locations, part_2, num_rows, num_cols):
    result = set()
    for locations in antenna_locations.values():
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
        for locations in antenna_locations.values():
            for location in locations:
                all_antinodes.add(location)
    return len(all_antinodes)

# Part 1 and Part 2
print(Solve(grid, False), Solve(grid, True)) # 390 1246
