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

def GenerateAntinodes(r1, c1, r2, c2, stop_after_first, num_rows, num_cols):
    if (r1, c1) == (r2, c2):
        raise ValueError("The antennas coincide")
    temp = []
    # Put r1, c1 on top
    if r1 <= r2:
        r1, c1, r2, c2 = r2, c2, r1, c1
    # r1, c1 => r2, c2 goes down and right
    if c1 < c2:
        rleft, cleft = r1 - (r2 - r1), c1 - (c2 - c1)
        rright, cright = r2 + (r2 - r1), c2 + (c2 - c1)
        temp.append((rleft, cleft))
        temp.append((rright, cright))
    # r1, c1 => r2, c2 goes down and left
    else:
        rleft, cleft = r2 + (r2 - r1), c2 - (c1 - c2)
        rright, cright = r1 - (r2 - r1), c1 + (c1 - c2)
        temp.append((rleft, cleft))
        temp.append((rright, cright))
    result = []
    for (r, c) in temp:
        if IsInBounds(r, num_rows) and IsInBounds(c, num_cols):
            result.append((r, c))
    return result


# Find all antinodes for all antennas.
def FindAllAntinodes(antenna_locations, stop_after_first, num_rows, num_cols):
    result = set()
    for antenna, locations in antenna_locations.items():
        if len(locations) < 2:
            continue
        for i in range(len(locations)):
            for j in range(i + 1, len(locations)):
                r1, c1 = locations[i]
                r2, c2 = locations[j]
                antinodes = GenerateAntinodes(r1, c1, r2, c2, stop_after_first, num_rows, num_cols)
                for antinode in antinodes:
                    result.add(antinode)
    return result

def Part1And2(grid, stop_after_first, count_antennas):
    antenna_locations = FindAntennaLocations(grid)
    kNumRows, kNumCols = NumRows(grid), NumCols(grid)
    all_antinodes = FindAllAntinodes(antenna_locations, stop_after_first, kNumRows, kNumCols)
    return len(all_antinodes) + (len(antenna_locations) if count_antennas else 0)

# Part 1
print(Part1And2(grid, True, False))

# Part 2
