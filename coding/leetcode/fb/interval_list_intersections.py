class Solution:
    def intervalIntersection(self, firstlist: list[list[int]], secondlist: list[list[int]]) -> list[list[int]]:

        size1 = len(firstlist)
        size2 = len(secondlist)

        if size1 == 0 or size2 == 0:
            return []

        index1 = 0
        index2 = 0

        def check_overlap(i1, i2):
            if i1[1] < i2[0] or i2[1] < i1[0]:
                return None
            return (max(i1[0], i2[0]), min(i1[1],i2[1]))

        result = []


        while 1:
            overlap = check_overlap(firstlist[index1], secondlist[index2])
            if overlap is not None:
                result.append(overlap)
            if index1+1 == size1 and index2+1 == size2:
                break
            if index1+1 == size1:
                index2 += 1
            elif index2+1 == size2:
                index1 += 1
            elif firstlist[index1][1] < secondlist[index2][1]:
                index1 += 1
            else:
                index2 += 1

        return result