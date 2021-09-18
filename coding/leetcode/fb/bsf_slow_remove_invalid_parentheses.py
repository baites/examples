from collections import deque as Deque

class Solution:

    @staticmethod
    def is_valid(s:str):
        counter = 0
        for c in s:
            if c == '(':
                counter += 1
            elif c == ')':
                counter -= 1
            if counter < 0:
                return False
        if counter > 0:
            return False
        return True

    def removeInvalidParentheses(self, s: str) -> list[str]:

        if self.is_valid(s):
            return (s,)

        # Set of valid candidates
        solutions = set()

        # Initiliza a queue with one string
        size = len(s)
        queue = Deque([s])

        while len(queue) > 0:

            # Get the next string
            s = queue.pop()
            if len(s) < size:
                if len(solutions) > 0:
                    break
                size = len(s)

            candidates = set()

            # Check removing one parenthesis
            for i in range(len(s)):
                if s[i] not in ('(', ')'):
                    continue
                subs = s[:i]+s[i+1:]
                if subs in candidates:
                    continue
                candidates.add(subs)
                # If valid string detected add to candidates
                if self.is_valid(subs):
                    solutions.add(subs)

            # If not add to the queue strings
            # with one of the parenthesis removed
            queue.extendleft(candidates)

        return solutions
