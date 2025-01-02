

def read_input(path: str) -> list[int]:
    output = []

    with open(path, 'r') as file:
        for line in file:
            for i in range(len(line)):
                output.append(int(line[i]))
    
    return output

def expand_map(disk_map: list[int]) -> list[tuple[int, int]]:
    result = []

    current_index = 0

    for i in range(len(disk_map)):
        if i % 2 == 0:
            result.append((current_index, i+1))
            current_index += 1
        else:
            result.append((-1, i+1))
    
    return result

def print_disk(disk: list[tuple[int, int]]) -> None:
    string = ""

    for id, amount in disk:
        if id == -1:
            string += '.'*amount
        else:
            string += str(id)*amount
    
    print(string)

if __name__ == '__main__':
    disk_map = read_input('test.txt')
    initial_disk = expand_map(disk_map)
    print_disk(initial_disk)