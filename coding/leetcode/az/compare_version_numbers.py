class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:

        # Split version to different revision
        version1 = version1.split('.')
        version2 = version2.split('.')

        index = 0

        while index < max(len(version1), len(version2)):

            v1 = int(version1[index]) if index < len(version1) else 0
            v2 = int(version2[index]) if index < len(version2) else 0

            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1

            index += 1

        return 0