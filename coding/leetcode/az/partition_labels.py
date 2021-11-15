class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        # map char location
        location = {char: index for index, char in enumerate(s)}

        partition = None
        previous = None
        partitions = []

        for index, char in enumerate(s):
            if partition is None or location[char] > partition:
                partition = location[char]
            if index == partition:
                size = partition+1 if previous is None else partition - previous
                partitions.append(size)
                previous = partition
                partition = None
        return partitions
