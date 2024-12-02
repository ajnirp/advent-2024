# python3 1.py < 1.txt

from collections import Counter

with open(0) as file:
    data = file.readlines()

left_list, right_list = [], []
for line in data:
    left, right = [int(n) for n in line.split()]
    left_list.append(left)
    right_list.append(right)

left_list.sort()
right_list.sort()

# Part 1
print(sum(abs(left - right) for left, right in zip(left_list, right_list)))

# Part 2
right_counter = Counter(right_list)
print(sum(right_counter[number] * number for number in left_list))
