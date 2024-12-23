from util import *

with open(0) as file:
    grid = [line.strip() for line in file.readlines()]

def Perimeter(r, c, grid, num_rows, num_cols):
    result = 0
    for nr, nc in Neighbors(r, c):
        if not (IsInBounds(nr, num_rows) and IsInBounds(nc, num_cols)):
            result += 1
        elif grid[nr][nc] != grid[r][c]:
            result += 1
    return result

def FencingPrice(r, c, grid, seen):
    kNumRows, kNumCols = NumRows(grid), NumCols(grid)
    kStartValue = grid[r][c]
    queue = [(r, c)]
    area, perimeter = 0, 0
    while queue:
        next_wave = []
        for (rr, cc) in queue:
            if seen[rr][cc]: continue
            seen[rr][cc] = True
            area += 1
            perimeter += Perimeter(rr, cc, grid, kNumRows, kNumCols)
            for nr, nc in ValidNeighbors(rr, cc, kNumRows, kNumCols):
                if grid[nr][nc] != kStartValue: continue
                next_wave.append((nr, nc))
        queue = next_wave
    return area * perimeter

def TotalFencingPrice(grid):
    kNumRows, kNumCols = NumRows(grid), NumCols(grid)
    seen = [[False for _ in range(kNumCols)] for _ in range(kNumRows)]
    total_price = 0
    for r in range(kNumRows):
        for c in range(kNumCols):
            if seen[r][c]: continue
            total_price += FencingPrice(r, c, grid, seen)
    return total_price

print(TotalFencingPrice(grid))  # 1457298
