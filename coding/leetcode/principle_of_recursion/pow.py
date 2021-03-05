class Solution:
    
    def __init__(self):
        self.mem = {}
    
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1.0/x
            n *= -1
            
        if n == 0:
            return 1.0
        if n == 1:
            return x
        
        if n in self.mem:
            return self.mem[n]
        
        self.mem[n] = self.myPow(x, n//2) * self.myPow(x, n-n//2)

        return self.mem[n]