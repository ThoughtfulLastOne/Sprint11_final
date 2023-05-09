# 87096682
from typing import List, Tuple


def get_distance(houses: List[int], n: int) -> List[int]:
    distanse = [n] * n
    zero = [i for i in range(n) if houses[i] == 0]
    first_zero = zero[0]
    last_zero = zero[-1]

    for i in range(first_zero, n):
        if houses[i] != 0:
            distanse[i] = distanse[i - 1] + 1
        else:
            distanse[i] = 0
    for i in range(last_zero, first_zero, -1):
        if houses[i] != 0:
            distanse[i] = min(distanse[i], distanse[i + 1] + 1)
        else:
            distanse[i] = 0
    for i in range(first_zero - 1, -1, -1):
        distanse[i] = distanse[i + 1] + 1
    return distanse


def read_input() -> Tuple[List[int], int]:
    n = int(input())
    houses = [int(num) for num in input().split()]
    return houses, n


if __name__ == '__main__':
    houses, n = read_input()
    print(" ".join(map(str, get_distance(houses, n))))
