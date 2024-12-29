from copy import deepcopy

with open(0) as file:
    lines = file.readlines()

def ParseRobot(line):
    def ParseChunk(chunk):
        return list(map(int, chunk[2:].split(',')))
    return list(map(ParseChunk, line.strip().split()))

def ParseRobots(lines):
    return list(map(ParseRobot, lines))

HEIGHT, WIDTH = 103, 101  # 14.txt
# HEIGHT, WIDTH = 7, 11  # 14t.txt
robots = ParseRobots(lines)

def Move(robots, steps):
    for i in range(len(robots)):
        (px, py), (vx, vy) = robots[i]
        px = (px + vx*steps) % WIDTH
        py = (py + vy*steps) % HEIGHT
        robots[i][0] = [px, py]

def SafetyFactor(robots):
    quadrants = [0] * 4
    for (px, py), _ in robots:
        # Ignore robots that are in the middle horizontally or vertically.
        if px == WIDTH//2 or py == HEIGHT//2: continue
        left = 0 <= px < WIDTH//2
        upper = 0 <= py < HEIGHT//2
        if left and upper: quadrants[0] += 1
        elif not left and upper: quadrants[1] += 1
        elif left and not upper: quadrants[2] += 1
        else: quadrants[3] += 1
    result = 1
    for q in quadrants: result *= q
    return result

def CreateGrid(robots):
    grid = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
    for (px, py), _ in robots:
        grid[py][px] += 1
    return grid

# Boolean heuristic to determine if `grid` looks like a Christmas tree when seen
# from above.
def ChristmasTreeHeuristic(grid):
    num_single_runs_of_five = 0
    for row in range(HEIGHT):
        run_length = 0
        only_one_run_of_five = False
        for col in range(WIDTH):
            run_length = run_length + 1 if grid[row][col] > 0 else 0
            if run_length == 5:
                only_one_run_of_five = not only_one_run_of_five
        if only_one_run_of_five:
            num_single_runs_of_five += 1
    return num_single_runs_of_five >= 10

def PrintGrid(grid):
    for h in range(HEIGHT):
        for w in range(WIDTH):
            print('.' if grid[h][w] == 0 else grid[h][w], end='')
        print()

def FindFirstChristmasTreeIteration(robots, max_num_steps):
    grid = CreateGrid(robots)
    num_steps = 0
    while num_steps < max_num_steps:
        if ChristmasTreeHeuristic(grid):
            PrintGrid(grid)
            return num_steps
        num_steps += 1
        Move(robots, 1)
    return -1

robots_copy = deepcopy(robots)
Move(robots, 100)
print(SafetyFactor(robots))  # 231852216
print(FindFirstChristmasTreeIteration(robots_copy, 50000))
