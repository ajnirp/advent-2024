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

# def PrintGrid(robots, width, height):
#     grid = [[0 for _ in range(width)] for _ in range(height)]
#     for (px, py), _ in robots:
#         grid[py][px] += 1
#     for h in range(height):
#         for w in range(width):
#             print('.' if grid[h][w] == 0 else grid[h][w], end='')
#         print()

Move(robots, 100)
# PrintGrid(robots, WIDTH, HEIGHT)
print(SafetyFactor(robots))
