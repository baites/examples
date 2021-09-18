import math

# Add any extra import statements you may need here


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

    print(t_count)

    size = len(s)
    length = -1

    for i in range(size):
        s_count = {}
        for j in range(i, size):
            s_count[s[j]] = s_count.setdefault(s[j], 0) + 1
            if comp(s_count, t_count):
                if length == -1:
                    length = j - i + 1
                else:
                    length = min(length, j - i + 1)

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

    s1 = "dcbefebce"
    t1 = "cdb"
    expected_1 = 5
    output_1 = min_length_substring(s1, t1)
    print(output_1)
    #check(expected_1, output_1)