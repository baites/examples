import math
# Add any extra import statements you may need here
from bisect import bisect_left

# Add any helper functions you may need here
def binary_search(array, value, lo):
  # Find the left most index with "value"
  left = bisect_left(array, value, lo=lo)
  if left != len(array) and array[left] == value:
    right = bisect_left(array, value+1, lo=left+1)
    return left, right
  return None, None

def numberOfWays(arr, k):
 	# Initilize counter
  counter = 0

  # Sort the array to reduce N^2 complexity
  arr.sort()

  # Loop over the array value
  for i, v in enumerate(arr):
    # Compute delta between k and v
    delta = k-v
    # If delta is less than one then out arr bound
    if delta < 1:
      break
    # if anothe element is found its value is delta
    # but delta + v = k or we found a pair
    left, right = binary_search(arr, delta, i+1)
    if left is None:
      continue
    counter += (right-left)

  return counter












# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def printInteger(n):
  print('[', n, ']', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printInteger(expected)
    print(' Your output: ', end='')
    printInteger(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  k_1 = 6
  arr_1 = [1, 2, 3, 4, 3]
  expected_1 = 2
  output_1 = numberOfWays(arr_1, k_1)
  check(expected_1, output_1)

  k_2 = 6
  arr_2 = [1, 5, 3, 3, 3]
  expected_2 = 4
  output_2 = numberOfWays(arr_2, k_2)
  check(expected_2, output_2)

  # Add your own test cases here