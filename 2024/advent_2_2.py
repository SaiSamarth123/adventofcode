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
    global total
    arr = np.array(arr)

    differences = np.abs(np.diff(arr))

    if np.all((1 <= differences) & (differences <= 3)):
        total += 1


def check_order(data):
    for line in data:
        array = list(map(int, line.split()))

        if array == sorted(array) or array == sorted(array, reverse=True):
            check_diff(array)


check_order(lines)
print(total)
