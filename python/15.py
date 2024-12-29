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
    # Child classes must implement these methods.
    def Move(self, move): pass
    def PrintGrid(self): pass
    def GpsCoordinate(self, row, col): return 0

    def Moves(self, moves):
        for move in moves: self.Move(move)

    def SumOfAllBoxGpsCoordinates(self):
        result = 0
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if self.grid[row][col] == 'O':
                    result += self.GpsCoordinate(row, col)
        return result

class Part1State(State):
    def __init__(self, grid):
        self.grid = grid
        self.num_rows, self.num_cols = NumRows(self.grid), NumCols(self.grid)
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
        if self.grid[row][col] == '.':
            self.robot.row, self.robot.col = row, col
            return
        elif self.grid[row][col] == '#':
            pass  # No movement.
            return
        # Find the first non-box along that direction. If it's an empty space,
        # move all the boxes there. We can simulate this by transferring the
        # first box to the empty spot.
        # If it's an obstacle, you can't move.
        dest_row, dest_col = row, col  # Where the robot wanted to move to.
        while self.grid[row][col] == 'O':
            row += dr
            col += dc
        if self.grid[row][col] == '#': pass  # Can't push the boxes.
        elif self.grid[row][col] == '.':
            self.grid[row][col] = 'O'
            self.grid[dest_row][dest_col] = '.'
            self.robot.SetPosition(dest_row, dest_col)

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
    
class Part2State(State):
    def __init__(self, grid):
        self.grid = self.InitializeGrid(grid)
        self.num_rows, self.num_cols = NumRows(grid), NumCols(grid)

    def InitializeGrid(self,grid):
        result = []
        for row in grid:
            for char in row:
                if char == '#':
                    result.append('#')
                    result.append('#')
                elif char == 'O':
                    result.append('[')
                    result.append(']')
                elif char == '.':
                    result.append('.')
                    result.append('.')
                elif char == '@':
                    result.append('@')
                    result.append('.')

    def Move(self, move):
        row, col = self.robot.GetPosition()
        dr, dc = DirectionVector(move)
        row += dr
        col += dc
        if self.grid[row][col] == '.':
            self.robot.row, self.robot.col = row, col
            return
        elif self.grid[row][col] == '#':
            pass  # No movement.
            return
        # Same algorithm as above, except now it's more complicated. One push
        # can move an unbounded number of boxes. The whole group moves as one,
        # and a single obstacle off to the side that abuts a single box can stop
        # the entire group from being pushed.
        # First we find out which boxes are being pushed, then we move all of
        # them one step in the direction of the vector.
        dest_row, dest_col = row, col  # Where the robot wanted to move to.
        # Handle horizontal and vertical movement separately.
        # Horizontal movement.
        if dr == 0:
            while self.grid[row][col] in '[]':
                col += dc
            if self.grid[row][col] == '#': pass  # Can't push the boxes.
            elif self.grid[row][col] == '.':
                pass  # TODO
            return
        # Vertical movement.
        # TODO.
        return


part_1_state = Part1State(grid)
part_1_state.Moves(moves)
print(part_1_state.SumOfAllBoxGpsCoordinates()) # 1294459
