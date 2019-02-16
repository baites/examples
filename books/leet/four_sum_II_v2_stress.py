class Naive(object):
    def fourSumCount(self, A, B, C, D):
        size = len(A)
        count = 0
        for iA in range(size):
            for iB in range(size):
                for iC in range(size):
                    for iD in range(size):
                        tsum = A[iA] + B[iB] + C[iC] + D[iD]
                        if tsum == 0:
                            count += 1
        return count


class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        size = len(A)
        A.sort()
        B.sort()
        C.sort()
        D.sort()

        cA = {}
        cB = {}
        cC = {}
        cd = {}
        cD = {}
        for i in range(size):
            cA[A[i]] = i
            cB[B[i]] = i
            cC[C[i]] = i
            cD[D[i]] = i

        SC = {}
        iC = 0
        while iC < size:
            vC = C[iC]
            iD = 0
            while iD < size:
                vD = D[iD]
                psum = vC + vD
                SC[psum] = SC.get(psum, 0) +\
                    (cD[vD] - iD + 1) * (cC[vC] - iC + 1)
                iD = cD[vD] + 1
            iC = cC[vC] + 1

        sA = 0
        iA = 0
        while iA < size:
            vA = A[iA]
            iB = 0
            sB = 0
            while iB < size:
                vB = B[iB]
                psum = vA + vB
                sC = SC.get(-psum, 0)
                sB += (cB[vB] - iB + 1) * sC
                iB = cB[vB] + 1
            sA += (cA[vA] - iA + 1) * sB
            iA = cA[vA] + 1
            sB = 0
        return sA


import random
import time

size = 40
vrange = 100

while 1:
    A = []; B = []; C = []; D = []
    for i in range(size):
        A.append(random.randint(-vrange, vrange))
        B.append(random.randint(-vrange, vrange))
        C.append(random.randint(-vrange, vrange))
        D.append(random.randint(-vrange, vrange))

    start = time.time()
    naive = Naive().fourSumCount(A, B, C, D)
    naive_time = time.time()
    solution = Solution().fourSumCount(A, B, C, D)
    solution_time = time.time()
    speedup = (naive_time - start)/\
                (solution_time - naive_time)
    print('naive: {}, solution {} (x{})'.format(
        naive, solution, speedup
    ))
    if naive == solution:
        print('ok')
    else:
        print(A)
        print(B)
        print(C)
        print(D)
        print('bad')
        break
