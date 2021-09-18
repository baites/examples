import math

# Add any extra import statements you may need here

# Add any helper functions you may need here
def sift_up(heap, index):
    while index > 0 and heap[(index - 1) // 2] > heap[index]:
        temp = heap[(index - 1) // 2]
        heap[(index - 1) // 2] = heap[index]
        heap[index] = temp
        index = (index - 1) // 2


def sift_down_3elem(heap):
    minindex = 0
    if heap[0] > heap[1]:
        minindex = 1
    if heap[minindex] > heap[2]:
        minindex = 2
    if minindex != 0:
        temp = heap[0]
        heap[0] = heap[minindex]
        heap[minindex] = temp


def heappush_3elem(heap, value):
    heap.append(value)
    sift_up(heap, len(heap) - 1)


def heappop_4elem(heap):
    heap[0] = heap.pop()
    sift_down_3elem(heap)


def findMaxProduct(arr):
    # Write your code here

    output = []
    heap = []

    for value in arr:
        heappush_3elem(heap, value)
        if len(heap) < 3:
            output.append(-1)
        elif len(heap) == 3:
            output.append(heap[0] * heap[1] * heap[2])
        else:
            heappop_4elem(heap)
            output.append(heap[0] * heap[1] * heap[2])

    return output


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
    arr_1 = [1, 2, 3, 4, 5]
    expected_1 = [-1, -1, 6, 24, 60]
    output_1 = findMaxProduct(arr_1)
    check(expected_1, output_1)

    arr_2 = [2, 4, 7, 1, 5, 3]
    expected_2 = [-1, -1, 56, 56, 140, 140]
    output_2 = findMaxProduct(arr_2)
    check(expected_2, output_2)

    # Add your own test cases here
