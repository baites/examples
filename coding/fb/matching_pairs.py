
# Add any helper functions you may need here


def matching_pairs(s, t):
  # Write your code here

  def delta(i,j):
    count = 0
    count -= 1 if s[i] == t[i] else 0
    count -= 1 if s[j] == t[j] else 0
    count += 1 if s[j] == t[i] else 0
    count += 1 if s[i] == t[j] else 0
    return count

  size = len(s)

  count = 0
  for i in range(size):
    count += 1 if s[i] == t[i] else 0

  max_match = 0
  for i in range(size):
    for j in range(i+1, size):
      max_match = max(max_match, count + delta(i,j))
  return max_match












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
  s_1, t_1 = "abcde", "adcbe"
  expected_1 = 5
  output_1 = matching_pairs(s_1, t_1)
  check(expected_1, output_1)

  s_2, t_2 = "abcd", "abcd"
  expected_2 = 2
  output_2 = matching_pairs(s_2, t_2)
  check(expected_2, output_2)

  # Add your own test cases here




