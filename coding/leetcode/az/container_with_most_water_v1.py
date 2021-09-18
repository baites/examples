class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1
        while left < right:
            width = right - left
            min_height = min(height[left], height[right])
            max_area = max(max_area, width * min_height)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area