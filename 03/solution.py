#!/usr/local/bin/python3
import re

# ==== PART 1 ====

mult = 0

with open('./input', 'r') as input:
    corpus = input.read()
    for M in re.finditer(r"mul\(([0-9]+),([0-9]+)\)", corpus):
        mult += int(M.group(1)) * int(M.group(2))
        
print(f"PART 1 - Result: {mult}")

# ==== PART 2 ====

mult = 0
enabled = True

with open('./input', 'r') as input:
    corpus = input.read()
    for M in re.finditer(r"(do)\(\)|(don't)\(\)|(mul)\(([0-9]+),([0-9]+)\)", corpus):
        enabled = (enabled and not M.group(2) == "don't") or (not enabled and M.group(1) == "do")
        if enabled and M.group(3) == "mul": mult += int(M.group(4)) * int(M.group(5))
        
print(f"PART 2 - Result: {mult}")