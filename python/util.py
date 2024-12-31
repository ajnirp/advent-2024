# Functions for dealing with 2-D arrays.
def NumRows(grid): return len(grid)
def NumCols(grid): return len(grid[0])  # Assumes `grid` is not empty.
def IsInBounds(idx, max_idx): return 0 <= idx < max_idx
def IsInGrid(r, max_r, c, max_c): return IsInBounds(r, max_r) and IsInBounds(c, max_c)
def Neighbors(r, c):
    drs = [-1,1,0,0]
    dcs = [0,0,1,-1]
    for dr, dc in zip(drs, dcs):
        yield (r+dr, c+dc)
def ValidNeighbors(r, c, num_rows, num_cols):
    for nr, nc in Neighbors(r, c):
        if IsInBounds(nr, num_rows) and IsInBounds(nc, num_cols):
            yield nr, nc
def PrintGrid(grid):
    num_rows, num_cols = NumRows(grid), NumCols(grid)
    for r in range(num_rows):
        for c in range(num_cols):
            print(grid[r][c], end='')
        print()