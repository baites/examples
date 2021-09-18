class Solution:
    def findStrobogrammatic(self, n: int) -> list[str]:

        if n == 1:
            return ["0", "1", "8"]
        if n == 2:
            return ["11", "69", "88", "96"]

        m = 3
        strobos1 = ["11", "69", "88", "96"]
        strobos2 = ["0", "1", "8"]

        while m <= n:
            strobos = []
            if m%2 == 1:
                for str1 in strobos1:
                    for str2 in ["0", "1", "8"]:
                        strobos.append(str1[:(m-1)//2] + str2 +str1[(m-1)//2:])
            else:
                for str1 in strobos2:
                    for str2 in ["00","11", "69", "88", "96"]:
                        strobos.append(str1[:(m-2)//2] + str2 +str1[(m-2)//2:])
            strobos2 = strobos1
            strobos1 = strobos
            m += 1

        return strobos