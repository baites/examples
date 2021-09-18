import math
# Add any extra import statements you may need here


# Add any helper functions you may need here
def comp(array_a, array_b, u, v):
  size = len(array_a)
  for i in range(u):
    if array_a[i] != array_b[i]:
      return False
  for i in range(u,v+1):
    if array_a[i] != array_b[v-i+u] and\
        array_a[i] != array_b[i]:
      return False
  for i in range(v+1,size):
    if array_a[i] != array_b[i]:
      return False
  return True

def precompute(array_a, array_b):

  size = len(array_a)

  E = [[False]*(size-i) for i in range(size)]
  R = [[False]*(size-i) for i in range(size)]

  for d in range(size):
    for s in range(size-d):
      if d in (0, 1):
        prevE = True
        prevR = True
      else:
        prevE = E[s+1][d-2]
        prevR = R[s+1][d-2]

      E[s][d] = prevE and \
        array_a[s] == array_b[s] and array_a[s+d] == array_b[s+d]
      R[s][d] = prevR and (\
         array_a[s] == array_b[s+d] and array_a[s+d] == array_b[s] or\
         array_a[s] == array_b[s] and array_a[s+d] == array_b[s+d]
      )

  return E, R


def comp2(E, R, u, v):
   size = len(E)
   leftE = True if u == 0 else E[0][u-1]
   rightE = True if v == size-1 else E[v+1][size-v-2]
   return leftE and R[u][v-u] and rightE


def are_they_equal(array_a, array_b):
  # Write your code here
  E,R = precompute(array_a, array_b)
  size = len(array_a)
  for i in range(size):
    for j in range(i, size):
      if comp2(E, R, i, j):
        return True
  return False










# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!
def printString(string):
  print('[\"', string, '\"]', sep='', end='')

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
    printString(expected)
    print(' Your output: ', end='')
    printString(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  n_1 = 4
  a_1 = [1, 2, 3, 4]
  b_1 = [1, 4, 3, 2]
  expected_1 = True
  output_1 = are_they_equal(a_1, b_1)
  check(expected_1, output_1)

  n_2 = 4
  a_2 = [1, 2, 3, 4]
  b_2 = [1, 2, 3, 5]
  expected_2 = False
  output_2 = are_they_equal(a_2, b_2)
  check(expected_2, output_2)

  # Add your own test cases here
