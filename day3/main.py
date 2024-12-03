import re

def read_input(path: str) -> list[list[int]]:
    mults = []

    with open(path, 'r') as file:
        for line in file:
            # for each line, extract each instance of "mul(x,y)"
            valid_muls = re.findall("mul\([0-9]+,[0-9]+\)", line)

            for mul in valid_muls:
                # for each instance of "mul(x,y)", extract x and y and cast them to int
                vals = re.findall("[0-9]+", mul)
                vals = list(map(int, vals))
                mults.append(vals)
    
    return mults

def read_input_part2(path: str) -> list[list[int]]:
    ops = []

    with open(path, 'r') as file:
        for line in file:
            valid_ops = re.findall("mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)", line)

            for op in valid_ops:
                if op == 'do()':
                    ops.append([1])
                elif op == "don't()":
                    ops.append([-1])
                else:
                    vals = re.findall("[0-9]+", op)
                    vals = list(map(int, vals))
                    ops.append(vals)
    
    return ops

if __name__ == '__main__':
    mults = read_input('input.txt')
    result1 = 0

    for mul in mults:
        if not len(mul) == 2:
            print("incorect number of arguments: " + str(len(mul)))
            break
        
        result1 += mul[0] * mul[1]
    
    print(f"Result part 1: {result1}")

    ops = read_input_part2('input.txt')
    result2 = 0
    index = 0

    while index < len(ops)-1:
        if len(ops[index]) == 1:
            if ops[index][0] == -1:
                while (not (len(ops[index]) == 1 and ops[index][0] == 1)) and index < len(ops)-1:
                    index += 1
                continue
            elif ops[index][0] == 1:
                index += 1
                continue

        if len(ops[index]) > 2:
            print("incorrect number of arguments: " + str(len(ops[index])))
            break

        result2 += ops[index][0] * ops[index][1]
        index += 1
    
    print(f"Result part 2: {result2}")


