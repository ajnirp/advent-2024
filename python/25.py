with open(0) as file:
    contents = file.read()

def ParseBlock(lines):
    return lines.strip().split('\n')

def Classify(blocks, locks, keys):
    if len(blocks) == 0: return
    num_rows = len(blocks[0])
    num_cols = len(blocks[0][0])
    for block in blocks:
        heights = []
        if block[0][0] == '#':
            for col in range(num_cols):
                row = 1
                while row < num_rows and block[row][col] == '#': row += 1
                heights.append(row - 1)
            locks.append(heights)
        else:
            for col in range(num_cols):
                row = num_rows - 1
                while row >= 0 and block[row][col] == '#': row -= 1
                heights.append(num_rows - row - 2)
            keys.append(heights)
    return num_rows - 2

blocks = [ParseBlock(block) for block in contents.split('\n\n')]
locks, keys = [], []

def Fits(key, lock, max_height):
    return all(k + l <= max_height for k, l in zip(key, lock))

def Part1():
    max_height = Classify(blocks, locks, keys)
    return sum(Fits(key, lock, max_height) for key in keys for lock in locks)

print(Part1())  # 3365
