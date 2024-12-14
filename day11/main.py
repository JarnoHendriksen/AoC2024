import numpy as np

cache = {}

def read_input(path: str) -> list[int]:
    with open(path, 'r') as file:
        for line in file:
            return list(map(int, line.split()))

def count_stones(stone: int, blinks: int) -> int:
    if (stone, blinks) in cache:
        return cache[(stone, blinks)]
    
    count = 0
    digits = str(stone)

    if blinks == 0:
        return 1
    
    if stone == 0:
        count = count_stones(1, blinks - 1)
    elif len(digits) % 2 == 0:
        half_length = int(len(digits) / 2)
        left = int(digits[:half_length])
        right = int(digits[half_length:])
        count = count_stones(left, blinks - 1) + count_stones(right, blinks - 1)
    else:
        count = count_stones(stone * 2024, blinks - 1)

    cache[(stone, blinks)] = count

    return count

def count_all_stones(stones: list[int], blinks: int) -> int:
    total = 0

    for s in stones:
        total += count_stones(s, blinks)
    
    return total

if __name__ == '__main__':
    stones = read_input('input.txt')
    result1 = count_all_stones(stones, 25)
    print(f"Result part 1: {result1}")
    result2 = count_all_stones(stones, 75)
    print(f"Result part 2: {result2}")
