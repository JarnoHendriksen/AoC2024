import numpy as np

def read_input(path: str) -> np.ndarray[int]:
    lines = []

    with open(path, 'r') as file:
        for line in file:
            lines.append(list(map(int, line.split())))
    
    return lines

def get_diffs(report: list[int]) -> list[int]:
    diffs = []

    for i in range(1, len(report)):
        diffs.append(report[i] - report[i-1])
    
    return diffs

def is_increasing(diffs: list[int]) -> bool:
    inc = 0

    for d in diffs:
        inc += np.sign(d)
    
    return inc > 0


def is_safe_without(index: int, report: list[int]) -> bool:
    values = report * 1
    del values[index]
    # print(values)
    diffs = get_diffs(values)
    sign = 1 if is_increasing(diffs) else -1

    for d in diffs:
        if (not np.sign(d) == sign) or np.abs(d) <= 0 or np.abs(d) > 3:
            return False
    return True

def is_safe_with_dampener(report: list[int]) -> bool:
    diffs = get_diffs(report)
    sign = 1 if is_increasing(diffs) else -1

    print("======")
    print(report)
    print(diffs)
    print(sign)

    for d in diffs:
        if (not np.sign(d) == sign) or np.abs(d) <= 0 or np.abs(d) > 3:
            for i in range(len(report)):
                if is_safe_without(i, report):
                    return True
            return False
    
    return True

if __name__ == '__main__':
    reports = read_input('input.txt')
    safe_reports = 0
    
    for r in reports:
        if is_safe_with_dampener(r):
            safe_reports += 1

    print(f"Result part 1: {safe_reports}")

