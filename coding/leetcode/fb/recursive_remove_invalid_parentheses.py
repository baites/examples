class Solution:

    def __init__(self):
        self.valid_expressions = None
        self.min_removed = None

    def reset(self, removed=float("inf")):
        self.valid_expressions = set()
        self.min_removed = removed


    def remaining(self, string, index, left, right, expression, removed):
        """
            string: The original string we are recursing on
            index: current index in the original string
            left: number of left parentheses till now
            right: number of right parentheses till now
            expression: the resulting expression in this particular recursion
            removed: number of parentheses removed in this particular recursion
        """
        # Check if it is the end of the string
        if index == len(string):

            # If it is a valid expression (is it though?)
            if left == right:

                # If removed is less or equal that minimal
                if removed <= self.min_removed:
                    # Removed is strictly less, reset valid expressions
                    if removed < self.min_removed:
                        self.reset(removed)
                    # Add the expression to the list of valid expressions
                    self.valid_expressions.add(''.join(expression))

        else:

            # Get current char
            char = string[index]

            # If char is not a parenthesis
            if char not in ['(',')']:
                # Add the character and keep recursing
                expression.append(char)
                self.remaining(
                    string, index+1,
                    left, right,
                    expression, removed
                )
                # Remove char after recursive exploration
                expression.pop()
            # If it is a parenthesis
            else:
                # Else

                # one recursion is done ignorign current char
                self.remaining(
                    string, index + 1,
                    left, right,
                    expression,
                    removed + 1
                )

                # the other expression is adding the char
                expression.append(char)

                if char == '(':
                    self.remaining(
                        string, index + 1,
                        left + 1, right,
                        expression, removed
                    )
                # Next option is right parenthesis
                # However, if no valid expression is
                # possible if right > left
                elif right < left:
                    self.remaining(
                        string, index + 1,
                        left, right + 1,
                        expression, removed
                    )

                # Remove char after recursive exploration
                expression.pop()


    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        # Reset the class level variables that we use for every test case.
        self.reset()

        # Recursive call
        self.remaining(s, 0, 0, 0, [], 0)
        return self.valid_expressions
