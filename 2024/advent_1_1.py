import re


# loop through the two lists based on the length
# sort the array
# get the distance at next index
# find the difference and add to the total distance
# print the total distance


def find_total(arr1, arr2):

    total_dist = 0

    for dist1, dist2 in zip(arr1, arr2):
        total_dist += -1 * (dist1 - dist2)

    return total_dist
