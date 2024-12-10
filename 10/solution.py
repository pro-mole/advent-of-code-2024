#!/usr/local/bin/python3

# ==== PART 1 ====

DIRS = [(0,1), (0,-1), (1,0), (-1,0)]
def trail_ends(map, x, y, step):
    if x < 0 or x >= len(map[0]) or y < 0 or y >= len(map):
        return set()
    
    if map[y][x] != step:
        return set()

    if step == 9:
        return {(x,y)}
    
    ends = set()
    for d in DIRS:
        ends = ends.union(trail_ends(map, x+d[0], y+d[1], step+1))
    return ends

def trail_rate(map, x, y, step):
    if x < 0 or x >= len(map[0]) or y < 0 or y >= len(map):
        return 0
    
    if map[y][x] != step:
        return 0

    if step == 9:
        return 1
    
    rating = 0
    for d in DIRS:
        rating += trail_rate(map, x+d[0], y+d[1], step+1)
    return rating

map = []

with open('./input', 'r') as input:
    for line in input.readlines():
        map.append([int(char) for char in line.strip()])

score_sum = 0

# Find Trailheads
trailheads = []
y = 0
for line in map:
    x = 0
    for number in line:
        if number == 0:
            trailheads.append((x,y))
        x += 1
    y += 1

for (hx, hy) in trailheads:
    score_sum += len(trail_ends(map, hx, hy, 0))

print(f"PART 1 - Solution {score_sum}")

# ==== PART 2 ====

rating_sum = 0

for (hx, hy) in trailheads:
    rating_sum += trail_rate(map, hx, hy, 0)

print(f"PART 2 - Solution {rating_sum}")
