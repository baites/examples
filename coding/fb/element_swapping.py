import math

# Add any extra import statements you may need here


def findMinArray(arr, k):
    # Write your code here
    size = len(arr)

    i = 0
    # Loop over swaps
    while k > 0 and i < size and i < k + 1:
        m = arr.index(min(arr[i : k + 1]))
        k -= m - i
        while m != i:
            temp = arr[m]
            arr[m] = arr[m - 1]
            arr[m - 1] = temp
            m -= 1
        i += 1
    return arr


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!


def printInteger(n):
    print("[", n, "]", sep="", end="")


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
    n_1 = 3
    arr_1 = [5, 3, 1]
    k_1 = 2
    expected_1 = [1, 5, 3]
    output_1 = findMinArray(arr_1, k_1)
    check(expected_1, output_1)

    n_2 = 5
    arr_2 = [8, 9, 11, 2, 1]
    k_2 = 3
    expected_2 = [2, 8, 9, 11, 1]
    output_2 = findMinArray(arr_2,k_2)
    check(expected_2, output_2)

    # Add your own test cases here
