#!/usr/local/bin/python3

# ==== PART 1 ====

calibration = 0

# Determine if the equation is solvable either with a '+' or a '*' between each operand
def solvable(R, ops):
    if len(ops) == 1:
        return R == ops[0]
    
    return solvable(R, [ops[0] + ops[1]] + ops[2:]) or solvable(R, [ops[0] * ops[1]] + ops[2:])

with open("./input", 'r') as input:
    for line in input.readlines():
        _res, _ops = line.split(": ")
        result = int(_res)
        operands = [int(op) for op in _ops.split(" ")]

        if solvable(result, operands):
            calibration += result

print(f"PART 1 - Solution: {calibration}")

# ==== PART 2 ====

calibration = 0

# Determine if the equation is solvable either with a '+', a '*' or a '||' between each operand
def solvable3(R, ops):
    if len(ops) == 1:
        return R == ops[0]
    
    return solvable3(R, [ops[0] + ops[1]] + ops[2:]) or solvable3(R, [ops[0] * ops[1]] + ops[2:]) or solvable3(R, [int(str(ops[0]) + str(ops[1]))] + ops[2:])

with open("./input", 'r') as input:
    for line in input.readlines():
        _res, _ops = line.split(": ")
        result = int(_res)
        operands = [int(op) for op in _ops.split(" ")]

        if solvable3(result, operands):
            calibration += result

print(f"PART 1 - Solution: {calibration}")