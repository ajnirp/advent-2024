# python3 2.py < 2.txt

with open(0) as file:
    file_contents = file.readlines()

data = []
for line in file_contents:
    row = [int(word) for word in line.split()]
    data.append(row)

# Copies the list `arr` to a new list, skipping the element at `i`.
def copy_with_index_skip(arr, i):
    return [elem for j, elem in enumerate(arr) if j != i]

# If `skips_remaining` is < 0, returns False right away. Otherwise, generates
# 2 candidate lists: one by skipping over the element at `i`, one by skipping
# over the element at `i+1`. Returns True if either works.
def try_with_two_candidates(arr, i, skips_remaining):
    if skips_remaining < 0:
        return False
    candidate1 = copy_with_index_skip(arr, i)
    candidate2 = copy_with_index_skip(arr, i+1)
    return is_safe(candidate1, skips_remaining) or is_safe(candidate2, skips_remaining)

# Returns True iff `row` is safe. Only does one pass over the list if
# `skips_remaining` is 0.
def is_safe(row, skips_remaining):
    if skips_remaining < 0:
        return False
    is_increasing = 'unset'
    for i in range(len(row) - 1):
        if not 1 <= abs(row[i] - row[i+1]) <= 3:
            return try_with_two_candidates(row, i, skips_remaining - 1)
        if row[i] < row[i+1]:
            if is_increasing == 'unset':
                is_increasing = 'yes'
            elif is_increasing == 'no':
                return try_with_two_candidates(row, i, skips_remaining - 1)
        elif row[i] > row[i+1]:
            if is_increasing == 'unset':
                is_increasing = 'no'
            elif is_increasing == 'yes':
                return try_with_two_candidates(row, i, skips_remaining - 1)
        # no need to check for equality: the jump check took care of that
    return True

print(sum(is_safe(row, 0) for row in data))
print(sum(is_safe(row, 1) for row in data))

# Potential optimization: use this class so that instead of copying over arrays
# we simply store references to them and which indices to skip. Not implemented
# for lack of time / interest.
class ArrayWithSkipIndices:
    def __init__(self, arr, skips=[]):
        self.arr = arr
        self.skips = skips
        if len(self.skips) > 1:
            raise ValueError("Not implemented: too many elements in skip array:", self.skips)

    def at(self, i):
        if not self.skips or i < self.skips[0]:
            return self.arr[i]
        return self.arr[i - skips[0] + 1]
