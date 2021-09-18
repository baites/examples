def rotationalCipher(input, rotation_factor):
    # Write your code here
    index_to_numeric = [chr(index) for index in range(ord("0"), ord("9") + 1)]
    index_to_lower = [chr(index) for index in range(ord("a"), ord("z") + 1)]
    index_to_upper = [chr(index) for index in range(ord("A"), ord("Z") + 1)]

    numeric_to_index = {
        chr(index): index - ord("0") for index in range(ord("0"), ord("9") + 1)
    }
    lower_to_index = {
        chr(index): index - ord("a") for index in range(ord("a"), ord("z") + 1)
    }
    upper_to_index = {
        chr(index): index - ord("A") for index in range(ord("A"), ord("Z") + 1)
    }

    cipher = ""

    numeric_size = len(index_to_numeric)
    lower_size = len(index_to_lower)
    upper_size = len(index_to_upper)

    for c in input:
        if c in numeric_to_index:
            cipher += index_to_numeric[
                (numeric_to_index[c] + rotation_factor) % numeric_size
            ]
        elif c in lower_to_index:
            cipher += index_to_lower[(lower_to_index[c] + rotation_factor) % lower_size]
        elif c in upper_to_index:
            cipher += index_to_upper[(upper_to_index[c] + rotation_factor) % upper_size]
        else:
            cipher += c

    return cipher


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
    input_1 = "All-convoYs-9-be:Alert1."
    rotation_factor_1 = 4
    expected_1 = "Epp-gsrzsCw-3-fi:Epivx5."
    output_1 = rotationalCipher(input_1, rotation_factor_1)
    check(expected_1, output_1)

    input_2 = "abcdZXYzxy-999.@"
    rotation_factor_2 = 200
    expected_2 = "stuvRPQrpq-999.@"
    output_2 = rotationalCipher(input_2, rotation_factor_2)
    check(expected_2, output_2)
