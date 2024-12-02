#!/usr/local/bin/python3

left = []
right = []

with open("./input", "r") as input:
    for line in input.readlines():
        l, r = line.split("   ")
        left.append(int(l))
        right.append(int(r))

# ==== PART 1 ====

diff_sum = 0

# Sort in place for now; we might need to copy-sort later
left.sort()
right.sort()

for i in range(len(left)):
    diff_sum += abs(right[i] - left[i])

print(f"PART 1 - SOLUTION: {diff_sum}")

# ==== PART 2 ====

similarity = 0

# Use a set so we can eliminate any numbers that are not in both lists
similar = set(left) & set(right)
for n in similar:
    similarity += left.count(n) * n * right.count(n)

print(f"PART 1 - SOLUTION: {similarity}")
