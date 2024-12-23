from util import *

with open(0) as file:
    grid = [[int(char) for char in line.strip()] for line in file.readlines()]

# Does a breadth-first search from `start` in `grid`. Returns the score and
# rating for `start`.
def Score(start, grid, part_1):
    if grid[start[0]][start[1]] != 0: return 0, 0
    kNumRows, kNumCols = NumRows(grid), NumCols(grid)
    peaks = set()  # Set of all peaks i.e. locations where the value is 9.
    rating = 0  # Number of paths from `start` to a peak.
    seen = set()  # Set of all cells seen during the search.
    queue = [start]  # Breadth-first search queue.
    while queue:
        next_wave = []
        for r, c in queue:
            for nr, nc in Neighbors(r, c):
                if not (IsInBounds(nr, kNumRows) and IsInBounds(nc, kNumCols)): continue
                if not grid[nr][nc] == grid[r][c] + 1: continue
                if part_1 and (nr, nc) in seen: continue
                if grid[nr][nc] == 9:
                    peaks.add((nr, nc))
                    rating += 1
                else: next_wave.append((nr, nc))
                if part_1: seen.add((nr, nc))
        queue = next_wave
    return len(peaks), rating

def Solve(grid, part_1):
    kNumRows, kNumCols = NumRows(grid), NumCols(grid)
    return sum(Score((r, c), grid, part_1)[0 if part_1 else 1] for r in range(kNumRows) for c in range(kNumCols))

print(Solve(grid, True), Solve(grid, False))  # 459 1034
