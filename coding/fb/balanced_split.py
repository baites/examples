import math

# Add any extra import statements you may need here


# Add any helper functions you may need here


def balancedSplitExists(arr):
    # Write your code here
    arr.sort()

    # Size of the problem
    size = len(arr)

    # Forward sums
    forward = [0] * size
    forward[0] = arr[0]
    # Backward sums
    backward = [0] * size
    backward[-1] = arr[-1]

    for index in range(1, size):
        forward[index] = arr[index] + forward[index - 1]
        backward[size - index - 1] = arr[size - index - 1] + arr[size - index]

    for index in range(size - 1):
        if forward[index] == backward[index + 1] and arr[index] < arr[index + 1]:
            return True

    return False


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!


def printString(string):
    print('["', string, '"]', sep="", end="")


test_case_number = 1


def check(expected, output):
    global test_case_number
    result = False
    if expected == output:
        result = True
    rightTick = "\u2713"
    wrongTick = "\u2717"
    if result:
        print(rightTick, "Test #", test_case_number, sep="")
    else:
        print(wrongTick, "Test #", test_case_number, ": Expected ", sep="", end="")
        printString(expected)
        print(" Your output: ", end="")
        printString(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    arr_1 = [2, 1, 2, 5]
    expected_1 = True
    output_1 = balancedSplitExists(arr_1)
    check(expected_1, output_1)

    arr_2 = [3, 6, 3, 4, 4]
    expected_2 = False
    output_2 = balancedSplitExists(arr_2)
    check(expected_2, output_2)

    # Add your own test cases here
