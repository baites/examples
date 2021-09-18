

DICTIONARY = { str(i-ord('A')+1):chr(i) for i in range(ord('A'), ord('Z')) }


def possible_decodings(nums):

    decoded_strings = []

    def backtrack(
        index, # Indext to the original string
        decode # Decoded string
    ):
        # Base case
        if index == len(nums):
            decoded_strings.append(''.join(decode))
        else:

            decode.append(DICTIONARY[nums[index]])
            backtrack(index+1, decode)
            decode.pop()

            if index < len(nums)-1 and \
                nums[index:index+2] in DICTIONARY:
                decode.append(DICTIONARY[nums[index:index+2]])
                backtrack(index+2, decode)
                decode.pop()

    backtrack(0, [])
    return decoded_strings

print(possible_decodings("121"))



