import math

# Add any extra import statements you may need here
from collections import deque

# Add any helper functions you may need here
def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


def minOperations(arr):
    # Write your code here

    # Check trivial case
    if is_sorted(arr):
        return 0

    # Get size of the problem
    size = len(arr)

    # Veto list
    veto = set([tuple(arr)])

    # See the queue with initial array
    queue = deque([(0, arr)])

    while len(queue) > 0:

        # Get next seed and its dist from
        # original seed.
        dist, seed = queue.pop()

        for i in range(size - 1):
            for j in range(i + 1, size):
                candidate = seed[:i] + list(reversed(seed[i : j + 1])) + seed[j + 1 :]
                if tuple(candidate) in veto:
                    continue
                if is_sorted(candidate):
                    return dist + 1
                veto.add(tuple(candidate))
                queue.appendleft((dist + 1, candidate))

    return None


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!


def printInteger(n):
    print("[", n, "]", sep="", end="")


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
        printInteger(expected)
        print(" Your output: ", end="")
        printInteger(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    n_1 = 5
    arr_1 = [1, 2, 5, 4, 3]
    expected_1 = 1
    output_1 = minOperations(arr_1)
    check(expected_1, output_1)

    n_2 = 3
    arr_2 = [3, 1, 2]
    expected_2 = 2
    output_2 = minOperations(arr_2)
    check(expected_2, output_2)

    # Add your own test cases here
    n_3 = 5
    arr_3 = [2, 3, 5, 4, 1]
    expected_3 = 3
    output_3 = minOperations(arr_3)
    check(expected_3, output_3)

