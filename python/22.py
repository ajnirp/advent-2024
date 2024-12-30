with open(0) as file:
    numbers = [int(line.strip()) for line in file.readlines()]

def Mix(value, secret):
    return value ^ secret

def Prune(secret):
    return secret % 16777216

def Step(secret):
    secret = Prune(Mix(secret * 64, secret))
    secret = Prune(Mix(secret // 32, secret))
    return Prune(Mix(secret * 2048, secret))

def Steps(secret, num_steps):
    for _ in range(num_steps):
        secret = Step(secret)
    return secret

def Part1(numbers):
    return sum(Steps(number, 2000) for number in numbers)

print(Part1(numbers))  # 18525593556