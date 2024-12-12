#!/usr/local/bin/python3
from collections import defaultdict

def iterate(stones, memo):
    new_stones = defaultdict(int)
    for stone in stones:
        if not stone in memo:
            if len(stone) % 2 == 0:
                mid = len(stone)//2
                memo[stone] = [str(int(stone[:mid])), str(int(stone[mid:]))]
            else:
                memo[stone] = [str(int(stone) * 2024)]

        for new_stone in memo[stone]:
            new_stones[new_stone] += stones[stone]
    
    return new_stones

if __name__ == "__main__":
    # ==== PART 1 ====

    stones = defaultdict(int)

    with open('./input', 'r') as input:
        for stone in input.readline().strip().split(" "):
            stones[stone] += 1

    next = {"0": ["1"]}

    for i in range(25):
        stones = iterate(stones, next)

    print(f"PART 1 - Solution {sum(stones.values())}")

    # ==== PART 2 ====

    for i in range(25,75):
        stones = iterate(stones, next)

    print(f"PART 2 - Solution {sum(stones.values())}")