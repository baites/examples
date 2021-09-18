import math

# Add any extra import statements you may need here
from collections import deque

# Add any helper functions you may need here


def min_length_substring(s, t):
    # Write your code here

    def comp(string_count, substring_count):
        for c in substring_count:
            if c not in string_count or string_count[c] < substring_count[c]:
                return False
        return True

    t_count = {}
    for c in t:
        t_count[c] = t_count.setdefault(c, 0) + 1

    size = len(s)
    length = -1
    left = 0
    right = 0
    queue = deque()
    s_count = {s[right]: 1}

    # Loop over the right index until
    # the end of the string (if possible)
    while right < size:
        # Save in a queue last every
        # possition of a char of t in s.
        if s[right] in t_count and right > 0:
            queue.appendleft(right)
            # Update s counter char stats
            s_count[s[right]] = s_count.setdefault(s[right], 0) + 1
        # Check if any chances of a subtring
        # matching stats if no continue
        if not comp(s_count, t_count):
            right += 1
            continue
        # If there is a matching update length
        length = right-left+1 if length < 0 else min(length, right-left+1)
        # Check if there is a location to
        # update the left index (break is not)
        if len(queue) == 0:
            break
        # Reduce counter by 1 for char in s[left]
        s_count[s[left]] -= 1
        # Update left counter
        left = queue.pop()
        right += 1

    return length

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
    s1 = "dcbefebce"
    t1 = "fd"
    expected_1 = 5
    output_1 = min_length_substring(s1, t1)
    check(expected_1, output_1)

    s2 = "bfbeadbcbcbfeaaeefcddcccbbbfaaafdbebedddf"
    t2 = "cbccfafebccdccebdd"
    expected_2 = -1
    output_2 = min_length_substring(s2, t2)
    check(expected_2, output_2)

# Add your own test cases here
    s3 = "dcbefebce"
    t3 = "cdb"
    expected_3 = 3
    output_3 = min_length_substring(s3, t3)
    check(expected_3, output_3)
