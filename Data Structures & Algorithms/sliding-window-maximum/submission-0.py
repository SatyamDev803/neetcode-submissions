from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        result = []
        candidate = deque()

        for right, value in enumerate(nums):
            startIndex = right - k + 1

            while candidate and candidate[0] < startIndex:
                candidate.popleft()

            while candidate and nums[candidate[-1]] < value:
                candidate.pop()

            candidate.append(right)

            if right >= k-1:
                result.append(nums[candidate[0]])

        return result
