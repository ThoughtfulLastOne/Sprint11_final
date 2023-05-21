# 87544422
from typing import List, Tuple


def get_max_points(matrix: List[str], k: int) -> int:
    points = 0
    count = {}
    K = k * 2
    for number in matrix:
        if number != '.':
            if number not in count:
                count[number] = 1
            else:
                count[number] += 1
    for number in count.values():
        if 0 < int(number) <= K:
            points += 1
    return points


def read_input() -> Tuple[List[str], int]:
    k = int(input())
    matrix = ''.join([input() for _ in range(4)])
    return matrix, k


if __name__ == '__main__':
    matrix, k = read_input()
    print(get_max_points(matrix, k))
