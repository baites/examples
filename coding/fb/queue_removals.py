import math

# Add any extra import statements you may need here
from collections import deque

# Add any helper functions you may need here


def findPositions(arr, x):
    # Write your code here

    # PLaceholder for result of the function
    result = []

    # Create a queue with tuple (index, value)
    queue = deque(enumerate(arr))

    # Implement all the iterations
    for _ in range(x):

        # Largest pair
        max_pair = None
        # Waiting in line queue
        buffer = deque()
        # Count number of pops
        count = 0

        # Firs step of the iteration
        # Pop left x elements
        while len(queue) > 0 and count < x:
            pair = queue.popleft()
            # pylint: disable=unsubscriptable-object
            if max_pair is None or pair[1] > max_pair[1]:
                max_pair = pair
            buffer.append(pair)
            count += 1

        # Unload the buffer
        while len(buffer) > 0:
            index, value = buffer.popleft()
            # Check if pair index is max_pair index
            if index == max_pair[0]:
                result.append(index + 1)
                continue
            value = value - 1 if value > 0 else value
            queue.append((index, value))

    return result


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
    n_1 = 6
    x_1 = 5
    arr_1 = [1, 2, 2, 3, 4, 5]
    expected_1 = [5, 6, 4, 1, 2]
    output_1 = findPositions(arr_1, x_1)
    check(expected_1, output_1)

    n_2 = 13
    x_2 = 4
    arr_2 = [2, 4, 2, 4, 3, 1, 2, 2, 3, 4, 3, 4, 4]
    expected_2 = [2, 5, 10, 13]
    output_2 = findPositions(arr_2, x_2)
    check(expected_2, output_2)

    # Add your own test cases here
