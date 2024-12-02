import numpy as np

def read_input(path: str) -> np.ndarray[int]:
    lines = []

    with open(path, 'r') as file:
        for line in file:
            lines.append(list(map(int, line.split())))
    
    return lines

def is_safe(report: list[int]) -> bool:
    # calculate first difference to determine if values should increase or decrease
    prev_diff = report[1] - report[0]

    # if first difference is too big or 0, immediately mark as unsafe
    if prev_diff == 0 or np.abs(prev_diff) > 3:
        return False
    
    for i in range(len(report)):
        if i == 0 or i == len(report) - 1:
            continue

        diff = report[i+1] - report[i]

        if not (np.sign(diff) == np.sign(prev_diff)):
            return False
        if diff == 0 or np.abs(diff) > 3:
            return False

        prev_diff = diff
    
    return True

if __name__ == '__main__':
    reports = read_input('input.txt')
    safe_reports = 0
    
    for r in reports:
        if is_safe(r):
            safe_reports += 1

    print(f"Result part 1: {safe_reports}")

