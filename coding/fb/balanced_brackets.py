import math

# Add any extra import statements you may need here


# Add any helper functions you may need here


def isBalanced(s):
    # Write your code here

    BRACKETS = {"}": "{", "]": "[", ")": "("}

    stack = []

    for c in s:
        if c in ("{", "[", "("):
            stack.append(c)
        elif c in ("}", "]", ")"):
            if c in BRACKETS:
                if len(stack) > 0 and BRACKETS[c] == stack[-1]:
                    stack.pop()
                else:
                    return False

    if len(stack) != 0:
        return False

    return True


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!


def printString(string):
    print('["', string, '"]', sep="", end="")


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
        printString(expected)
        print(" Your output: ", end="")
        printString(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    s1 = "{[(])}"
    expected_1 = False
    output_1 = isBalanced(s1)
    check(expected_1, output_1)

    s2 = "{{[[(())]]}}"
    expected_2 = True
    output_2 = isBalanced(s2)
    check(expected_2, output_2)

    # Add your own test cases here
