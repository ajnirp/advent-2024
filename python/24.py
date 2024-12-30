with open(0) as file:
    lines = [line.strip() for line in file.readlines()]

def ParseInitialValues(lines, values):
    for line in lines:
        wire, value = line.split(': ')
        values[wire] = int(value)

def ParseGates(lines, gates):
    for line in lines:
        lhs, rhs = line.split(' -> ')
        in1, op, in2 = lhs.split()
        gates[rhs] = (op, in1, in2)

data_break_index = lines.index('')
values = {}
gates = {}
ParseInitialValues(lines[:data_break_index], values)
ParseGates(lines[(data_break_index+1):], gates)

def Evaluate(wire, values, gates):
    if wire in values: return values[wire]
    if wire in gates:
        op, in1, in2 = gates[wire]
        in1_value = Evaluate(in1, values, gates)
        in2_value = Evaluate(in2, values, gates)
        result = None
        if op == 'AND': result = in1_value & in2_value
        elif op == 'OR': result = in1_value | in2_value
        else: result = in1_value ^ in2_value
        values[wire] = result
        return result
    raise ValueError('Wire neither in values nor gates', wire)

def AllZWires(gates):
    wires = [wire for wire in gates if wire.startswith('z')]
    wires.sort(reverse=True)
    return wires

def Part1(values, gates):
    result = 0
    for wire in AllZWires(gates):
        result <<= 1
        result += Evaluate(wire, values, gates)
    return result

print(Part1(values, gates))
