class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        maxLeft = 0
        maxRight = 0

        water = 0

        while left <= right:
            if maxLeft <= maxRight:
                maxLeft = max(maxLeft, height[left])
                water += (maxLeft - height[left])
                left += 1
            else:
                maxRight = max(maxRight, height[right])
                water += (maxRight - height[right])
                right -= 1

        return water