with open(0) as file:
    lines = file.readlines()

class Computer:
    def __init__(self, lines):
        self.registers = []
        self.ParseLines(lines)
        self.program = self.ParseProgram(lines[-1])
        self.output = []
        self.opcode_to_impl = {
            0: self.adv,
            1: self.bxl,
            2: self.bst,
            3: self.jnz,
            4: self.bxc,
            5: self.out,
            6: self.bdv,
            7: self.cdv,
        }

    def ParseLines(self, lines):
        def ParseRegister(line):
            return int(line.strip().split(': ')[1])
        for i in range(3):
            self.registers.append(ParseRegister(lines[i]))

    def ParseProgram(self, line):
        return list(map(int, line.strip().split(': ')[1].split(',')))
    
    def Combo(self, op):
        if 0 <= op <= 3:
            return op
        elif 4 <= op <= 6:
            return self.registers[op - 4]
        else:
            raise ValueError('Unexpected combo operand', op)
    
    def RenderOutput(self):
        print('Program output:', ','.join(self.output))

    def RunProgram(self):
        self.instr_ptr = 0
        while True:
            if self.instr_ptr >= len(self.program):
                break
            opcode = self.program[self.instr_ptr]
            jumped = self.opcode_to_impl[opcode]()
            if not jumped:
                self.instr_ptr += 2
        self.RenderOutput()

    # Instructions' implementations.
    def dv(self, register_index):
        arg = self.Combo(self.program[self.instr_ptr + 1])
        self.registers[register_index] = self.registers[0] >> arg
    def adv(self): self.dv(0)
    def bdv(self): self.dv(1)
    def cdv(self): self.dv(2)
    def bxl(self):
        self.registers[1] ^= self.program[self.instr_ptr + 1]
    def bst(self):
        arg = self.Combo(self.program[self.instr_ptr + 1])
        self.registers[1] = arg % 8
    def jnz(self):
        if self.registers[0] == 0:
            return False  # no jump
        self.instr_ptr = self.program[self.instr_ptr + 1]
        return True  # did jump
    def bxc(self):
        self.registers[1] ^= self.registers[2]
    def out(self):
        arg = self.Combo(self.program[self.instr_ptr + 1])
        self.output.append(str(arg % 8))
    
computer = Computer(lines)
computer.RunProgram()
# print(computer.program, computer.registers)