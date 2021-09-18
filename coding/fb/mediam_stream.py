import math

# Add any extra import statements you may need here


# Add any helper functions you may need here


def heapify(heap, root, index):
    parent = (index - root - 1) // 2 + root
    while index > root and heap[parent] > heap[index]:
        heap[parent], heap[index] = heap[index], heap[parent]
        index = parent
        parent = (index - root - 1) // 2 + root


def findMedian(arr):
    # Write your code here
    # Placeholder for mediams
    mediams = []
    heap = []
    # Loop over the stream
    for value in arr:
        # Push element to the heap
        heap.append(value)
        length = len(heap)
        heapify(heap, 0, length - 1)
        # Implement a heapsort in place
        root = 0
        while root < length - 1:
            heap[root], heap[length - 1] = heap[length - 1], heap[root]
            heapify(heap, root, length - 1)
            root += 1
        if length % 2 == 0:
            mediams.append((heap[length // 2] + heap[length // 2 - 1]) // 2)
        else:
            mediams.append(heap[length // 2])
        length += 1
    return mediams


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
    arr_1 = [5, 15, 1, 3]
    expected_1 = [5, 10, 5, 4]
    output_1 = findMedian(arr_1)
    check(expected_1, output_1)

    arr_2 = [2, 4, 7, 1, 5, 3]
    expected_2 = [2, 3, 4, 3, 4, 3]
    output_2 = findMedian(arr_2)
    check(expected_2, output_2)

    # Add your own test cases here
