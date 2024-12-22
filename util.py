# Functions for dealing with 2-D arrays.
def NumRows(grid): return len(grid)
def NumCols(grid): return len(grid[0])  # Assumes `grid` is not empty.
def IsInBounds(idx, max_idx): return 0 <= idx < max_idx