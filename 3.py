# python3 3.py < 3.txt

import bisect
import re

with open(0) as file:
    data = file.read().strip()

DO_REGEX = r'do\(\)'
DONT_REGEX = r'don\'t\(\)'
MUL_REGEX = r'mul\((\d+),(\d+)\)'

# Part 1
print(sum(int(a)*int(b) for a, b in re.findall(MUL_REGEX, data)))

# Works a bit like classic merge in mergesort, but discards runs of elements
# that come from the same array, instead keeping only the lowest value.
# Example: intersperse([0, 2, 10], [3, 4]) would return [0, 3, 10].
# Classic merge would return [0, 2, 3, 4, 10].
def intersperse(dos, donts):
    result = [0] # Initially we have an implicit "do" at index 0.
    i, j = 0, 0
    last_was_a_do = True
    while i < len(dos) and j < len(donts):
        if dos[i] < donts[j]:
            # Only append if the last element was a "don't".
            if not last_was_a_do:
                result.append(dos[i])
                last_was_a_do = True
            i += 1
        # No need to check for equality, the two arrays cannot have a common
        # value.
        else:
            # Only append if the last element was a "do".
            if last_was_a_do:
                result.append(donts[j])
                last_was_a_do = False
            j += 1
    result.append(dos[i] if i < len(dos) else donts[j])
    return result

def find_start_indices(pattern, string):
    return [match.start(0) for match in re.finditer(pattern, data)]
dos = find_start_indices(DO_REGEX, data)
donts = find_start_indices(DONT_REGEX, data)
matches = [(match.start(0), int(match.group(1)), int(match.group(2))) for match in re.finditer(MUL_REGEX, data)]
flips = intersperse(dos, donts)

# Iterates over `matches`, using `flips` to determine if a match should be
# included in the result.
def part2(matches, flips):
    result = 0
    match_idx, flip_idx = 0, 0
    while match_idx < len(matches):
        match = matches[match_idx]
        # Find the largest flip value that's less than the match start index
        flip_idx = bisect.bisect_left(flips, match[0], flip_idx, len(flips)) - 1
        # Increment the result if we're in a "do"
        if flip_idx % 2 == 0:
            result += match[1] * match[2]
        match_idx += 1
    return result

# part 2
print(part2(matches, flips))
