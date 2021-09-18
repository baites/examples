class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # Set of chars in a substring
        location = {}

        # Define left and right indexes
        left = 0
        right = 0

        # Placeholder for maximum length
        max_length = 0

        # Loop over the string
        while left <= right and right < len(s):
            c = s[right]
            # If repeated char is found
            # move right and update left to right
            # reset the subse
            if c in location:
                next_left = location[c]+1
                for sc in s[left:next_left]:
                    del location[sc]
                left = next_left
                location[c] = right
            # Else check maxlength updates
            else:
                max_length = max(max_length, right-left+1)
                location[c] = right
            right += 1

        return max_length