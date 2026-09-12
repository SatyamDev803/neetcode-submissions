class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if num - 1 not in numSet:
                current = 1
                next_num = num + 1
                while next_num in numSet:
                    current += 1
                    next_num += 1
                if current > longest:
                    longest = current
                    
        return longest
