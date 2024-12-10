#!/usr/local/bin/python3

# ==== PART 1 ====

DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]

obstacles = set()
guard = None
map_size = None

with open('./input', 'r') as input:
    y = 0
    for line in input.readlines():
        x = 0
        for char in line:
            if char == "#":
                obstacles.add((x, y))
            if char == "^":
                guard = (x, y)
            x += 1
        y += 1
    map_size = (x-1,y)

passed = {guard}
direction_i = 0
turns = 0
while True:
    # Look for the closest obstacle in the current patrol direction
    direction = DIRS[direction_i]
    look = [guard[0] + direction[0], guard[1] + direction[1]]
    # Check tiles in the patrol direction until we reach an obstacle or leave the map
    while not tuple(look) in obstacles and look[0] > 0 and look[1] > 0 and look[0] < map_size[0] and look[1] < map_size[1]:
        passed.add(tuple(look))
        look[0] += direction[0]
        look[1] += direction[1]
    
    guard = (look[0]-direction[0], look[1]-direction[1])

    if tuple(look) in obstacles: # Did we find an obstacle?
        # Cycle direction
        direction_i = (direction_i + 1) % len(DIRS)
        turns += 1
    else:
        break

print(f"PART 1 - Solution: {len(passed)}")

# ==== PART 2 ====

# Proceed like Part 1, but while finding the guard's path, note the direction they were walking through that space
# At every space, check if adding an obstacle in front of the guard will make them turn towards a known part of the path, causing a loop

# Reset only the guard position
with open('./input', 'r') as input:
    y = 0
    for line in input.readlines():
        x = 0
        for char in line:
            if char == "^":
                guard = (x, y)
            x += 1
        y += 1

passed = {guard: {0}}
new_obstacles = set()
direction_i = 0
while True:
    # Look for the closest obstacle in the current patrol direction
    direction = DIRS[direction_i]
    look = [guard[0] + direction[0], guard[1] + direction[1]]
    # Check tiles in the patrol direction until we reach an obstacle or leave the map
    while not tuple(look) in obstacles and look[0] > 0 and look[0] < map_size[0] and look[1] > 0 and look[1] < map_size[1]:
        if not tuple(look) in passed:
            passed[tuple(look)] = set()
        
        # Check if adding an obstacle in front would start a loop
        next_direction = (direction_i + 1) % len(DIRS)
        predicted_step = (look[0], look[1])
        while not predicted_step in obstacles and predicted_step[0] > 0 and predicted_step[0] < map_size[0] and predicted_step[1] > 0 and predicted_step[1] < map_size[1]:
            if predicted_step in passed and next_direction in passed[predicted_step]:
                new_ob = (look[0] + direction[0], look[1] + direction[1])
                if not new_ob in obstacles:
                    new_obstacles.add(new_ob)
                break
            predicted_step = (predicted_step[0] + DIRS[next_direction][0], predicted_step[1] + DIRS[next_direction][1])
        
        passed[tuple(look)].add(direction_i)
        
        look[0] += direction[0]
        look[1] += direction[1]
    
    guard = (look[0]-direction[0], look[1]-direction[1])

    if tuple(look) in obstacles: # Did we find an obstacle?
        # Cycle direction
        direction_i = (direction_i + 1) % len(DIRS)
    else:
        break

print(f"PART 2 - Solution: {len(new_obstacles)}")