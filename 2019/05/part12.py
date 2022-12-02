def parse_opcode(opcode):
    opcode = str(opcode)

    opcode_type = int(opcode[-2:])
    opcode_addr_modes = list(map(lambda x: bool(int(x)), opcode[:-2]))
    opcode_addr_modes.reverse()

    # Addressing Mode: False -> Position, True -> Immediate

    return {
        "type": opcode_type,
        "addr_modes": opcode_addr_modes,
    }

def get_with_addr_mode(mem, val, addr_mode):
    if addr_mode == False:
        return mem[val]
    return val

def compute(mem, inputs):
    pc = 0
    outputs = []

    while True:
        opcode = parse_opcode(mem[pc])
        addr_modes = opcode["addr_modes"] + ([False] * (4 - len(opcode["addr_modes"])))

        # ADD OP1, OP2, [ADDR]
        if opcode["type"] == 1:
            op1 = get_with_addr_mode(mem, mem[pc+1], addr_modes[0])
            op2 = get_with_addr_mode(mem, mem[pc+2], addr_modes[1])
            dest = mem[pc+3]

            mem[dest] = op1 + op2
            pc += 4

        # MULT OP1, OP2, [ADDR]
        elif opcode["type"] == 2:
            op1 = get_with_addr_mode(mem, mem[pc+1], addr_modes[0])
            op2 = get_with_addr_mode(mem, mem[pc+2], addr_modes[1])
            dest = mem[pc+3]

            mem[dest] = op1 * op2
            pc += 4

        # INPUT [ADDR]
        elif opcode["type"] == 3:
            op1 = mem[pc+1]

            mem[op1] = inputs.pop(0)
            pc += 2

        # OUTPUT [ADDR]
        elif opcode["type"] == 4:
            op1 = mem[pc+1]

            outputs.append(mem[op1])
            pc += 2

        # JPNZ OP1, TARGET
        elif opcode["type"] == 5:
            op1 = get_with_addr_mode(mem, mem[pc+1], addr_modes[0])
            target = get_with_addr_mode(mem, mem[pc+2], addr_modes[1])

            if op1 != 0:
                pc = target
            else:
                pc += 3

        # JPZ OP1, TARGET
        elif opcode["type"] == 6:
            op1 = get_with_addr_mode(mem, mem[pc+1], addr_modes[0])
            target = get_with_addr_mode(mem, mem[pc+2], addr_modes[1])

            if op1 == 0:
                pc = target
            else:
                pc += 3

        # LT OP1, OP2, [DEST]
        elif opcode["type"] == 7:
            op1 = get_with_addr_mode(mem, mem[pc+1], addr_modes[0])
            op2 = get_with_addr_mode(mem, mem[pc+2], addr_modes[1])
            target = mem[pc+3]
            ans = int(op1 < op2)

            mem[target] = ans
            pc += 4

        # EQ OP1, OP2, [DEST]
        elif opcode["type"] == 8:
            op1 = get_with_addr_mode(mem, mem[pc+1], addr_modes[0])
            op2 = get_with_addr_mode(mem, mem[pc+2], addr_modes[1])
            target = mem[pc+3]
            ans = int(op1 == op2)

            mem[target] = ans
            pc += 4

        # HALT
        elif opcode["type"] == 99:
            break

        else:
            print(f"I don't know this opcode -> {mem[pc]}")
            exit(1)

    return outputs

if __name__ == "__main__":
    with open ("input.txt", "r") as f:
        mem = [int(x) for x in f.read().split(",")]
        mem = [int(x) for x in "3,9,8,9,10,9,4,9,99,-1,8".split(",")]
        
        outputs = compute(mem, inputs=[5])

        print(outputs)

"""
--- Part Two ---
The air conditioner comes online! Its cold air feels good for a while, but then the TEST alarms start to go off. Since the air conditioner can't vent its heat anywhere but back into the spacecraft, it's actually making the air inside the ship warmer.

Instead, you'll need to use the TEST to extend the thermal radiators. Fortunately, the diagnostic program (your puzzle input) is already equipped for this. Unfortunately, your Intcode computer is not.

Your computer is only missing a few opcodes:

Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
Opcode 6 is jump-if-false: if the first parameter is zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
Opcode 7 is less than: if the first parameter is less than the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
Opcode 8 is equals: if the first parameter is equal to the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
Like all instructions, these instructions need to support parameter modes as described above.

Normally, after an instruction is finished, the instruction pointer increases by the number of values in that instruction. However, if the instruction modifies the instruction pointer, that value is used and the instruction pointer is not automatically increased.

For example, here are several programs that take one input, compare it to the value 8, and then produce one output:

3,9,8,9,10,9,4,9,99,-1,8 - Using position mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).
3,9,7,9,10,9,4,9,99,-1,8 - Using position mode, consider whether the input is less than 8; output 1 (if it is) or 0 (if it is not).
3,3,1108,-1,8,3,4,3,99 - Using immediate mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).
3,3,1107,-1,8,3,4,3,99 - Using immediate mode, consider whether the input is less than 8; output 1 (if it is) or 0 (if it is not).
Here are some jump tests that take an input, then output 0 if the input was zero or 1 if the input was non-zero:

3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9 (using position mode)
3,3,1105,-1,9,1101,0,0,12,4,12,99,1 (using immediate mode)
Here's a larger example:

3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99
The above example program uses an input instruction to ask for a single number. The program will then output 999 if the input value is below 8, output 1000 if the input value is equal to 8, or output 1001 if the input value is greater than 8.

This time, when the TEST diagnostic program runs its input instruction to get the ID of the system to test, provide it 5, the ID for the ship's thermal radiator controller. This diagnostic test suite only outputs one number, the diagnostic code.

What is the diagnostic code for system ID 5?
"""
