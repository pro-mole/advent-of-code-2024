#!/usr/local/bin/python3

# ==== PART 1 ====

filesystem = []

with open("./input", 'r') as input:
    is_file = True
    file_id = 0
    for number in input.readline():
        if number == "\n": break

        for i in range(int(number)):
            filesystem.append(file_id if is_file else None)
        if is_file: file_id += 1
        is_file = not is_file

# Re-position files at end to fill the empty spaces
left = 0
right = len(filesystem) - 1

while left < right:
    while filesystem[left] != None:
        left += 1
    while filesystem[right] == None:
        right -= 1
    
    if left >= right: break

    filesystem[left], filesystem[right] = filesystem[right], filesystem[left]
    left += 1
    right -= 1

# Calcualte Checksum
checksum = 0

for pos in range(len(filesystem)):
    if filesystem[pos] == None: break # Only valid for part 1 (all empty spaces to the right)

    checksum += pos * filesystem[pos]

print(f"PART 1 - Solution {checksum}")

# ==== PART 2 ====

filesystem = []
last_file = 0

with open("./input", 'r') as input:
    is_file = True
    file_id = 0
    for number in input.readline():
        if number == "\n": break

        filesystem.append([file_id if is_file else None, int(number)])
        if is_file:
            last_file = file_id
            file_id += 1
        is_file = not is_file

# Re-position files at end to fill the empty spaces all at once
# TODO Optimize it so we don't need to look for the files from the end every time
while last_file > 0:
    # Find file in disk
    pos = len(filesystem)-1
    while filesystem[pos][0] == None or filesystem[pos][0] > last_file:
        pos -= 1
    
    cur = pos
    size = filesystem[pos][1]

    pos = 0
    while pos < cur:
        if filesystem[pos][0] == None:
            if filesystem[pos][1] >= size:
                filesystem[cur][0] = None
                filesystem[pos][0] = last_file
                if filesystem[pos][1] > size:
                    remaining = filesystem[pos][1] - size
                    filesystem[pos][1] = size
                    filesystem.insert(pos+1, [None, remaining])
                break
        pos += 1
    
    last_file -= 1

# Calculate Checksum
checksum = 0

pos = 0
for block in filesystem:
    file, size = block
    if file:
        checksum += file * sum(range(pos, pos+size))
    pos += size

print(f"PART 2 - Solution {checksum}")