#!/usr/local/bin/python3

# ==== PART 1 ====

antennas = {}
map_size = [0, 0]

with open("./input", 'r') as input:
    y = 0
    for line in input.readlines():
        x = 0
        for char in line:
            if char == '\n': break
            if char != '.':
                if not char in antennas:
                    antennas[char] = []
                antennas[char].append((x,y))
            x += 1
            map_size[0] = max(map_size[0], x)
        y += 1
        map_size[1] = max(map_size[1], y)

antinodes = set()

for freq in antennas:
    antenna_list = antennas[freq]
    for i in range(len(antenna_list)-1):
        for j in range(i+1, len(antenna_list)):
            # Antennas
            A1 = antenna_list[i]
            A2 = antenna_list[j]
            dist = (A2[0]-A1[0], A2[1]-A1[1])

            # Antinodes
            a1 = (A1[0]-dist[0], A1[1]-dist[1])
            a2 = (A2[0]+dist[0], A2[1]+dist[1])

            if a1[0] >= 0 and a1[0] < map_size[0] and a1[1] >= 0 and a1[1] < map_size[1]:
                antinodes.add(a1)
            if a2[0] >= 0 and a2[0] < map_size[0] and a2[1] >= 0 and a2[1] < map_size[1]:
                antinodes.add(a2)

print(f"PART 1 - Solution: {len(antinodes)}")

# ==== PART 2 ====

antinodes = set()

for freq in antennas:
    antenna_list = antennas[freq]
    for i in range(len(antenna_list)-1):
        for j in range(i+1, len(antenna_list)):
            # Antennas
            A1 = antenna_list[i]
            A2 = antenna_list[j]
            antinodes.add(tuple(A1))
            antinodes.add(tuple(A2))
            dist = (A2[0]-A1[0], A2[1]-A1[1])

            # Antinodes
            a1 = (A1[0]-dist[0], A1[1]-dist[1])
            while a1[0] >= 0 and a1[0] < map_size[0] and a1[1] >= 0 and a1[1] < map_size[1]:
                antinodes.add(a1)
                a1 = (a1[0]-dist[0], a1[1]-dist[1])            
            
            a2 = (A2[0]+dist[0], A2[1]+dist[1])
            while a2[0] >= 0 and a2[0] < map_size[0] and a2[1] >= 0 and a2[1] < map_size[1]:
                antinodes.add(a2)
                a2 = (a2[0]+dist[0], a2[1]+dist[1])            

print(f"PART 2 - Solution: {len(antinodes)}")
