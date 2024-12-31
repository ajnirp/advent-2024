from collections import defaultdict

with open(0) as file:
    numbers = [int(line.strip()) for line in file.readlines()]

def Step(num):
    PRUNE_MASK = 16777215
    num ^= (num << 6) & PRUNE_MASK
    num ^= (num >> 5) & PRUNE_MASK
    num ^= (num << 11) & PRUNE_MASK
    return num

def Solve(numbers):
    sequences, seen = defaultdict(int), set()
    part1 = 0
    for num in numbers:
        seen = set()
        window = []
        for step in range(2000):
            next_num = Step(num)
            window.append((next_num % 10) - (num % 10))
            num = next_num
            if len(window) == 4:
                if (sequence := tuple(window)) not in seen:
                    sequences[sequence] += next_num % 10
                    seen.add(sequence)
                window.pop(0)
        part1 += num
    part2 = max(sequences.values())
    return part1, part2

print(Solve(numbers))  # (18525593556, 2089)
