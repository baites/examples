class Solution:
     def divide(self, dividend: int, divisor: int) -> int:

        # Constants to account for 32 bit
        # interger arithmethic
        MAX_INT = 2147483647        # 2**31 - 1
        MIN_INT = -2147483648       # -2**31

        # Check for absolute value of
        # divisor is not larger than dividend
        if abs(divisor) > abs(dividend):
            return 0

        # Check for 32bit overflow (no possible in python3)
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        # Compute the sign
        # Uses -varible as -1 * variable
        negatives = 0
        if dividend < 0:
            negatives += 1
            dividend = -dividend

        if divisor < 0:
            negatives += 1
            divisor = -divisor

        # Special case the rest of divisor by 1
        if divisor == 1:
            if negatives == 1:
                return -dividend
            return dividend

        # Search for initial quotient and product
        # Uses bit shift operator as way
        # to multiply by power of 2.
        quotient = 1
        product = divisor
        while product <= dividend:
            product = product << 1
            quotient = quotient << 1

        # Binary search

        # Variables to follow quotient values
        left = quotient >> 1
        middle = left
        right = quotient

        # Variables to follow the product of
        # divisor times quotient
        left_product = product >> 1
        middle_product = left_product
        right_product = product

        # Binary search loop
        while dividend - left_product >= divisor:
            middle = (left+right) >> 1
            middle_product = (left_product+right_product) >> 1
            if middle_product <= dividend:
                left = middle
                left_product = middle_product
            else:
                right = middle
                right_product = middle_product

        # Ajusting signs
        if negatives == 1:
            return -middle

        return middle


print(Solution().divide(7,-3))