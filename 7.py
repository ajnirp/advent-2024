# python3 7.py < 7.txt

def ParseLine(line):
    left, right = line.split(':')
    left = int(left)
    right = [int(num) for num in right.strip().split()]
    return left, right

with open(0) as file:
    data = [ParseLine(line) for line in file.readlines()]

def CanSatisfy1(left, right):
    kNumBits = len(right) - 1
    for i in range(1 << kNumBits):
        binary_string = bin(i)[2:].rjust(kNumBits, '0')
        result = right[0]
        for j, char in enumerate(binary_string):
            if char == '0':
                result += right[j + 1]
            else:
                result *= right[j + 1]
        if result == left:
            return True
    return False

# Returns a string
def ConvertToBase(number, base):
    if base >= 10:
        raise ValueError("I can only convert numbers to bases < 10")
    result = []
    while number > 0:
        result.append(str(number % base))
        number //= base
    return ''.join(reversed(result))

# Converts `number` to `base` and returns it as a string.
def ConvertToBase(number, base):
    if base >= 10:
        raise ValueError("I can only deal with bases < 10")
    result = []
    while number > 0:
        result.append(str(number % base))
        number //= base
    return ''.join(reversed(result))

# Returns one less than the number represented by `array`. Destructively updates
# `array`.
# `array` represents a number in base `base`, read left to right. For example,
# `110` represents 30 in base 5.
def Decrement(array, base):
    if base >= 10:
        raise ValueError("I can only deal with bases < 10")
    if all(elem == '0' for elem in array):
        return ValueError("The number to decrement must be > 0")
    index = len(array) - 1
    while index >= 0:
        if array[index] != '0':
            array[index] = str(int(array[index]) - 1)
            return
        array[index] = str(base - 1)
        index -= 1

# Generates all numbers in base `base` as strings up to the numer `upper` but
# not including `upper`. Returns in descending order.
def AllNumbersUpTo(upper, base):
    if upper <= 0:
        raise ValueError("`upper` must be > 0")
    current = ConvertToBase(upper-1, base)
    num_digits = len(current)
    yield current
    current_array = list(current)
    for number in range(upper-2, -1, -1):
        Decrement(current_array, base)
        yield ''.join(current_array)

# Not very fast: takes 1m18s on my 2018 laptop.
# Not sure if there's a more optimal approach.
def CanSatisfy2(left, right):
    # Try an early exit: see if the LHS is too small.
    if left < sum(right):
        return False
    # Try an early exit: See if the LHS is too large.
    product = 1
    for number in right:
        product *= number
    if product < left:
        return False
    kNumDigits = len(right) - 1
    for ternary_string in AllNumbersUpTo(3 ** kNumDigits, 3):
        result = right[0]
        for j, char in enumerate(ternary_string):
            if char == '0':
                result += right[j + 1]
            elif char == '1':
                result *= right[j + 1]
            else:
                result = int(str(result) + str(right[j + 1]))
        if result == left:
            return True
    return False

def Part1(data):
    return sum(left if CanSatisfy1(left, right) else 0 for left, right in data)

def Part2(data):
    return sum(left if CanSatisfy2(left, right) else 0 for left, right in data)

print(Part1(data)) # 2654749936343
print(Part2(data))
