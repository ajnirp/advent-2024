from util import *

with open(0) as file:
    lines = [line.strip() for line in file.readlines()]

def ParseGridAndMoves(lines):
    grid = []
    for index, line in enumerate(lines):
        if line == '':
            return grid, ''.join(lines[index:])
        grid.append([char for char in line])
        
grid, moves = ParseGridAndMoves(lines)

def DirectionVector(move):
    MOVES = '><^v'
    RESULTS = [(0,1), (0,-1), (-1,0), (1,0)]
    return RESULTS[MOVES.index(move)]

class Robot:
    def __init__(self): pass
    def SetPosition(self, row, col): self.row, self.col = row, col
    def GetPosition(self): return self.row, self.col

class State:
    def __init__(self, grid):
        self.grid = grid
        self.num_rows, self.num_cols = NumRows(grid), NumCols(grid)
        self.robot = Robot()
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if grid[row][col] == '@':
                    self.robot.SetPosition(row, col)
                    # We found the robot. Write over that cell.
                    self.grid[row][col] = '.'

    def Move(self, move):
        row, col = self.robot.GetPosition()
        dr, dc = DirectionVector(move)
        row += dr
        col += dc
        if self.grid[row][col] == '.': self.robot.row, self.robot.col = row, col
        elif self.grid[row][col] == '#': pass  # No movement.
        # Find the first non-box along that direction. If it's an empty space,
        # move all the boxes there. We can simulate this by transferring the
        # first box to the empty spot.
        # If it's an obstacle, you can't move.
        else:
            # Where the robot originally wanted to move to.
            dest_row, dest_col = row, col
            while self.grid[row][col] == 'O':
                row += dr
                col += dc
            if self.grid[row][col] == '#': pass  # Can't push the boxes.
            elif self.grid[row][col] == '.':
                self.grid[row][col] = 'O'
                self.grid[dest_row][dest_col] = '.'
                self.robot.SetPosition(dest_row, dest_col)

    def Moves(self, moves):
        for move in moves: self.Move(move)

    def PrintGrid(self):
        robot_row, robot_col = self.robot.GetPosition()
        self.grid[robot_row][robot_col] = '@'
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                print(self.grid[row][col], end='')
            print()
        self.grid[robot_row][robot_col] = '.'

    def GpsCoordinate(self, row, col):
        return 100*row + col
    
    def SumOfAllBoxGpsCoordinates(self):
        result = 0
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if self.grid[row][col] == 'O':
                    result += self.GpsCoordinate(row, col)
        return result

state = State(grid)
state.Moves(moves)
print(state.SumOfAllBoxGpsCoordinates())
