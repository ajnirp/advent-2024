with open(0) as file: lines = file.readlines()

# Converts a set of lines specifying a machine config to a 3-tuple.
# The tuple contains (a_x, a_y), (b_x, b_y), (prize_x, prize_y)
def ParseMachineConfig(machine_config):
    def ParseLine(line):
        x, y = line.split(': ')[1].split(', ')
        x, y = int(x[2:]), int(y[2:])
        return x, y
    line_a, line_b, line_prize = machine_config
    ax, ay = ParseLine(line_a)
    bx, by = ParseLine(line_b)
    px, py = ParseLine(line_prize)
    return [(ax, bx), (ay, by), [px, py]]

# From `lines` representing the file input, extract out all machine configs.
def ExtractMachineConfigs(lines):
    # The `1` in `1 + len(lines)` is needed to get the final case.
    return [ParseMachineConfig(lines[i:i+3]) for i in range(0, 1+len(lines), 4)]

machine_configs = ExtractMachineConfigs(lines)

A_COST, B_COST, PRIZE_SHIFT = 3, 1, 10000000000000

# Returns the number of tokens required to get the prize for a machine.
def TokensRequired(machine_config):
    (ax, bx), (ay, by), (px, py) = machine_config
    denominator = ay*bx - ax*by
    if denominator == 0: return 0
    a = (py*bx - px*by) / denominator  # number of times to press A.
    b = (px*ay - py*ax) / denominator  # number of times to press B.
    if a != int(a) or b != int(b): return 0  # no floats.
    a, b = int(a), int(b)
    return A_COST*int(a) + B_COST*int(b)

def Solve(machine_configs):
    return sum(TokensRequired(config) for config in machine_configs)

def ShiftPrizes(machine_configs):
    for config in machine_configs:
        config[-1][0] += PRIZE_SHIFT
        config[-1][1] += PRIZE_SHIFT

print(Solve(machine_configs))  # 37128
ShiftPrizes(machine_configs)
print(Solve(machine_configs))  # 74914228471331
