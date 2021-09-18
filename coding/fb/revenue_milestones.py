import math

# Add any extra import statements you may need here


# Add any helper functions you may need here
def search(array, value):
    left = 0
    right = len(array)

    while left < right:
        middle = (left + right) // 2
        if array[middle] < value:
            left = middle + 1
        else:
            right = middle
    if left < len(array):
        return left
    return -2


def getMilestoneDays(revenues, milestones):
    # Write your code here

    # Precompute the sum of revenues on each
    # day (numeric integration)
    totals = [0] * len(revenues)
    totals[0] = revenues[0]
    for i in range(1, len(revenues)):
        totals[i] = totals[i - 1] + revenues[i]

    result = []
    for milestone in milestones:
        result.append(search(totals, milestone) + 1)

    return result


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!


def printIntegerList(array):
    size = len(array)
    print("[", end="")
    for i in range(size):
        if i != 0:
            print(", ", end="")
        print(array[i], end="")
    print("]", end="")


test_case_number = 1


def check(expected, output):
    global test_case_number
    expected_size = len(expected)
    output_size = len(output)
    result = True
    if expected_size != output_size:
        result = False
    for i in range(min(expected_size, output_size)):
        result &= output[i] == expected[i]
    rightTick = "\u2713"
    wrongTick = "\u2717"
    if result:
        print(rightTick, "Test #", test_case_number, sep="")
    else:
        print(wrongTick, "Test #", test_case_number, ": Expected ", sep="", end="")
        printIntegerList(expected)
        print(" Your output: ", end="")
        printIntegerList(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    revenues_1 = [100, 200, 300, 400, 500]
    milestones_1 = [300, 800, 1000, 1400]
    expected_1 = [2, 4, 4, 5]
    output_1 = getMilestoneDays(revenues_1, milestones_1)
    check(expected_1, output_1)

    revenues_2 = [700, 800, 600, 400, 600, 700]
    milestones_2 = [3100, 2200, 800, 2100, 1000]
    expected_2 = [5, 4, 2, 3, 2]
    output_2 = getMilestoneDays(revenues_2, milestones_2)
    check(expected_2, output_2)

    # Add your own test cases here
