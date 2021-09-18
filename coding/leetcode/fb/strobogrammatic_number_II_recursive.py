class Solution:
    def findStrobogrammatic(self, n: int) -> list[str]:

        if n == 1:
            return ["0", "1", "8"]
        if n == 2:
            return ["11", "69", "88", "96"]

        strobos = []

        if n%2 == 1:
            for str1 in self.findStrobogrammatic(n-1):
                for str2 in ["0", "1", "8"]:
                    strobos.append(str1[:(n-1)//2] + str2 +str1[(n-1)//2:])
        else:
            for str1 in self.findStrobogrammatic(n-2):
                for str2 in ["00","11", "69", "88", "96"]:
                    strobos.append(str1[:(n-2)//2] + str2 +str1[(n-2)//2:])

        return strobos