# python3 4.py < 4.txt

with open(0) as file:
    data = [line.strip() for line in file.readlines()]

def IsInBounds(idx, max_idx):
    return 0 <= idx < max_idx

def Part1(data):
    WORD = 'XMAS'
    num_rows = len(data)
    num_cols = len(data[0])
    result = 0
    DIRECTION_VECTORS = [(x, y) for x in [-1,0,1] for y in [-1,0,1] if (x, y) != (0, 0)]
    for row in range(num_rows):
        for col in range(num_cols):
            for dr, dc in DIRECTION_VECTORS:
                letters = []
                for i in range(len(WORD)):
                    r = row + dr * i
                    c = col + dc * i
                    if IsInBounds(r, num_rows) and IsInBounds(c, num_cols):
                        letters.append(data[r][c])
                candidate = ''.join(letters)
                result += candidate == WORD
    return result

# part 1
print(Part1(data))

def Part2(data):
    WORD = 'MAS'  # expected to have odd length
    REVERSE_WORD = 'SAM'
    half_len = len(WORD) // 2  # round down
    candidate_iter_range = range(-half_len, half_len + 1)
    num_rows = len(data)
    num_cols = len(data[0])
    result = 0
    for row in range(half_len, num_rows - half_len):
        for col in range(half_len, num_cols - half_len):
            first = ''.join(data[row+di][col+di] for di in candidate_iter_range)
            second = ''.join(data[row+di][col-di] for di in candidate_iter_range)
            result += all(candidate in [WORD, REVERSE_WORD] for candidate in [first, second])
    return result

# part 2
print(Part2(data))
