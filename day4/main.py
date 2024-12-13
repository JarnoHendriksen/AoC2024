import numpy as np
import regex as re

def read_input(path: str) -> tuple[str, tuple[int, int]]:
    result = ""
    with open(path, 'r') as file:
        result = file.read()

    lines = result.split('\n')
    width = len(lines[0])
    height = len(lines)
    
    return (result, (width, height))

def find_word(word: str, input: str, size: tuple[int, int]) -> list[str]:
    puzzle = re.sub("\n", "", input)
    print(puzzle)
    
    rev_word = word[::-1]
    horizontal = re.findall(f"{word}|{rev_word}", puzzle, overlapped=True)
    re_vert = ""
    for i in range(len(word)):
        re_vert += word[i]
        re_vert += ".{" + str(size[0]-1) + "}" if i < len(word)-1 else ""
    re_vert += "|"

    for i in range(len(rev_word)):
        re_vert += rev_word[i]
        re_vert += ".{" + str(size[0]-1) + "}" if i < len(rev_word)-1 else ""
    vertical = re.findall(re_vert, puzzle, overlapped=True)

    re_diag1 = ""
    for i in range(len(word)):
        re_diag1 += word[i]
        re_diag1 += ".{" + str(size[0]-2) + "}" if i < len(word)-1 else ""
    re_diag1 += "|"

    for i in range(len(rev_word)):
        re_diag1 += rev_word[i]
        re_diag1 += ".{" + str(size[0]-2) + \
            "}" if i < len(rev_word)-1 else ""
    diagonal1 = re.findall(re_diag1, puzzle, overlapped=True)

    re_diag2 = ""
    for i in range(len(word)):
        re_diag2 += word[i]
        re_diag2 += ".{" + str(size[0]) + "}" if i < len(word)-1 else ""
    re_diag2 += "|"

    for i in range(len(rev_word)):
        re_diag2 += rev_word[i]
        re_diag2 += ".{" + str(size[0]) + "}" if i < len(rev_word)-1 else ""
        
    print(re_diag2)
    diagonal2 = re.findall(re_diag2, puzzle, overlapped=True)

    return len(horizontal) + len(vertical) + len(diagonal1) + len(diagonal2)

if __name__ == '__main__':
    puzzle, size = read_input('test.txt')
    matches = find_word('XMAS', puzzle, size)
    print(matches)