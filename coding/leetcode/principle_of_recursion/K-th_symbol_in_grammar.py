class Solution:
    
    FUNCTION = {0: [1, 0], 1:[0, 1]}
    
    def kthGrammar(self, N: int, K: int) -> int:
        if N == 1:
            return 0
        grammar = self.kthGrammar(N-1, K//2 + K % 2)
        return self.FUNCTION[grammar][K % 2]            