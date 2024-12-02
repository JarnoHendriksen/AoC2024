import numpy as np

def read_input(path: str) -> tuple[list[int], list[int]]:
    l1 = []
    l2 = []
    with open(path, 'r') as file:
        for line in file:
            split_string = line.split()
            l1.append(int(split_string[0]))
            l2.append(int(split_string[1]))
    
    return (np.array(l1), np.array(l2))

def count_occurrences(l2: list[int]) -> dict[int, int]:
    sums = {}

    for i in l2:
        if not i in sums:
            sums[i] = 1
        else:
            sums[i] += 1
    
    return sums

def get_similarity_score(l1: list[int], l2: list[int]) -> int:
    sum = 0
    l2_occurences = count_occurrences(l2)

    for i in l1:
        sum += i * l2_occurences.get(i, 0)

    return sum


if __name__ == '__main__':
    l1, l2 = read_input('input.txt')
    l1, l2 = (np.sort(l1), np.sort(l2))
    dists = np.absolute(l1 - l2)
    result1 = np.sum(dists)
    print(f"Result part 1: {result1}")
    result2 = get_similarity_score(l1, l2)
    print(f"Result part 2: {result2}")
