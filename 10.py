from util import *

with open(0) as file:
    grid = [[int(char) for char in line.strip()] for line in file.readlines()]

# Does a breadth-first search from `start` in `grid`. Returns the score for that
# trailhead.
def Score(start, grid):
    start_r, start_c = start
    if grid[start_r][start_c] != 0:
        return 0
    kNumRows, kNumCols = NumRows(grid), NumCols(grid)
    queue = [start]
    peaks = set()
    result = 0
    while queue:
        next_wave = []
        for r, c in queue:
            for nr, nc in Neighbors(r, c):
                if not (IsInBounds(nr, kNumRows) and IsInBounds(nc, kNumCols)):
                    continue
                if not grid[nr][nc] == grid[r][c] + 1: continue
                if grid[nr][nc] == 9: peaks.add((nr, nc))
                else: next_wave.append((nr, nc))
        queue = next_wave
    return len(peaks)

def Part1(grid):
    kNumRows, kNumCols = NumRows(grid), NumCols(grid)
    return sum(Score((r, c), grid) for r in range(kNumRows) for c in range(kNumCols))

print(Part1(grid))
