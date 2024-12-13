import numpy as np

def read_input(path: str) -> np.ndarray[int]:
    grid = []

    with open(path, 'r') as file:
        for line in file:
            gridline = []
            for i in range(len(line)):
                if not line[i].isnumeric():
                    continue
                gridline.append(int(line[i]))
            
            grid.append(gridline)
    
    grid = np.array(grid)

    return grid

def find_starting_points(grid: np.ndarray[int]) -> list[np.ndarray[int]]:
    points = []
    for y in range(grid.shape[0]):
        for x in range(grid.shape[1]):
            if grid[y, x] == 0:
                points.append([y, x])
    return points


def traverse_grid(grid: np.ndarray[int], starting_points: np.ndarray[int]) -> tuple[int, np.ndarray[int]]:
    stack = []
    right = np.array([0, 1])
    down = np.array([1, 0])

    number_of_endpoints = 0
    number_of_paths = 0

    for s in starting_points:
        stack.append(s)

        reachable_from_s = []

        while len(stack) > 0:
            current_pos = stack.pop()
            left_coord = current_pos - right
            right_coord = current_pos + right
            up_coord = current_pos - down
            down_coord = current_pos + down
            
            if left_coord[1] >= 0:
                if grid[left_coord[0], left_coord[1]] == grid[current_pos[0], current_pos[1]] + 1:
                    stack.append(left_coord)
                    #print(f"Left: {left_coord}")
            if right_coord[1] < grid.shape[1]:
                if grid[right_coord[0], right_coord[1]] == grid[current_pos[0], current_pos[1]] + 1:
                    stack.append(right_coord)
                    #print(f"Right: {right_coord}")
            if up_coord[0] >= 0:
                if grid[up_coord[0], up_coord[1]] == grid[current_pos[0], current_pos[1]] + 1:
                    stack.append(up_coord)
                    #print(f"Up: {up_coord}")
            if down_coord[0] < grid.shape[0]:
                if grid[down_coord[0], down_coord[1]] == grid[current_pos[0], current_pos[1]] + 1:
                    stack.append(down_coord)
                    #print(f"Down: {down_coord}")
            
            pos_index = current_pos[0] + current_pos[1] * grid.shape[1]

            if grid[current_pos[0], current_pos[1]] == 9:
                if not pos_index in reachable_from_s:
                    reachable_from_s.append(pos_index)
                    number_of_endpoints += 1
                
                number_of_paths += 1

        reachable_from_s = []
    
    return (number_of_endpoints, number_of_paths)

if __name__ == '__main__':
    grid = read_input('input.txt')
    print(grid)
    starting_points = find_starting_points(grid)
    endpoints, paths = traverse_grid(grid, starting_points)

    print(f"Result part 1: {endpoints}")
    print(f"Result part 2: {paths}")