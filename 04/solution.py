#!/usr/local/bin/python3

# ==== PART 1 ====

SEARCH_VECTORS = [
    (1, 0),
    (1, 1),
    (0, 1),
    (-1, 1),
    (-1, 0),
    (-1, -1),
    (0, -1),
    (1, -1)
]

letter_grid = []
word_count = 0

# Search word in grid starting at position (x, y)
# Return: number of words found (0-8)
def search_8dir(word, grid, x, y):
    found = 8
    for D in SEARCH_VECTORS:
        _x = x
        _y = y
        for i in range(len(word)):
            if _x < 0 or x >= len(grid[0]) or _y < 0 or _y >= len(grid):
                found -= 1
                break

            if grid[_y][_x] == word[i]:
                _y += D[1]
                _x += D[0]
            else:
                found -= 1
                break

    return found

with open('./input', 'r') as input:
    letter_grid = input.readlines()

# Position in the grid
x = 0
y = 0
for line in letter_grid:
    x = 0
    for letter in line:
        if letter == 'X':
            word_count += search_8dir('XMAS', letter_grid, x, y)
        x += 1
    y += 1

print(f"PART 1 - Solution: {word_count}")

# ==== PART 2 ====

SEARCH_XVECTORS = [
    (1, 1),
    (-1, 1)
]

word_count = 0

# Check if an X of words is found with center at position (x, y)
# Return: if the patter is valid
def search_xpattern(word, grid, x, y):
    for D in SEARCH_XVECTORS:
        dx = 0
        dy = 0
        mid = len(word)//2
        for i in range(mid+1):
            if x-dx < 0 or x+dx >= len(grid[0]) or y-dy < 0 or y+dy >= len(grid):
                return False

            # This solution is, in fact, incomplete
            # It works for a 3-leter word (MAS) but can find false positives for larger words
            if (grid[y+dy][x+dx] == word[mid+i] and grid[y-dy][x-dx] == word[mid-i]) or (grid[y-dy][x-dx] == word[mid+i] and grid[y+dy][x+dx] == word[mid-i]):
                dy += D[1]
                dx += D[0]
            else:
                return False

    return True

# Position in the grid
x = 0
y = 0
for line in letter_grid:
    x = 0
    for letter in line:
        if letter == 'A':
            word_count += 1 if search_xpattern('MAS', letter_grid, x, y) else 0
        x += 1
    y += 1

print(f"PART 2 - Solution: {word_count}")
