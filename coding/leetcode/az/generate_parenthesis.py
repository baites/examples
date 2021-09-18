class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        solutions = []
        solution = ['']*(2*n)

        # Recursive generation
        def generate(left=n, right=n, index=0):
            # Invalid partial string
            if left > right:
                return
            # I have balanced string
            if left == 0 and right == 0:
                solutions.append(''.join(solution))
                return
            # Explore if you can add more left parenthesis
            if left > 0:
                solution[index] = '('
                generate(left - 1, right, index+1)
            # Explore if you can add more right parenthesis
            if right > 0:
                solution[index] = ')'
                generate(left, right - 1, index+1)

        # Call recursion
        generate()

        # Return solutions
        return solutions