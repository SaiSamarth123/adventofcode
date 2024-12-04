import numpy as np

input = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""


lines = input.strip().split("\n")

total = 0


def check_diff(arr):

    n = len(arr)

    bad_level = 0

    for i in range(1, n):

        if not (1 <= abs(arr[i] - arr[i - 1]) <= 3):

            bad_level += 1

            if bad_level > 1:
                return False

            if i > 1 and not (1 <= abs(arr[i] - arr[i - 2]) <= 3):
                return False

    return True


def check_order(data):
    global total
    for line in data:
        array = list(map(int, line.split()))

        if array == sorted(array) or array == sorted(array, reverse=True):
            if check_diff(array):
                total += 1


check_order(lines)
print(total)
