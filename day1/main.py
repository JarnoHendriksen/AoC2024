import numpy as np

listpair = tuple[np.ndarray[int], np.ndarray[int]]

def read_input(path: str) -> listpair:
    l1 = []
    l2 = []
    with open(path, 'r') as file:
        for line in file:
            split_string = line.split()
            l1.append(int(split_string[0]))
            l2.append(int(split_string[1]))
    
    return (np.array(l1), np.array(l2))

def sort_lists(l: listpair) -> listpair:
    return (np.sort(l[0]), np.sort(l[1]))

def get_distances(l: listpair) -> np.ndarray[int]:
    return np.absolute(l[0] - l[1])

def count_occurrences(l2: list[int]) -> dict[int, int]:
    sums = {}

    for i in l2:
        if not i in sums:
            sums[i] = 1
        else:
            sums[i] += 1
    
    return sums

def get_similarity_score(l: listpair) -> int:
    sum = 0
    l2_occurences = count_occurrences(l[1])

    for i in l[0]:
        sum += i * l2_occurences.get(i, 0)

    return sum


if __name__ == '__main__':
    input_lists = read_input('input.txt')
    sorted_lists = sort_lists(input_lists)
    dists = get_distances(sorted_lists)
    result1 = np.sum(dists)
    print(f"Result part 1: {result1}")
    result2 = get_similarity_score(sorted_lists)
    print(f"Result part 2: {result2}")
