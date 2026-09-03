class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count frequencies.
        frequency = {}
        for num in nums:
            frequency[num] = 1 + frequency.get(num, 0)
        # Put each number into a bucket based on its frequency.
        bucket = defaultdict(list)
        for num, freq in frequency.items():
            bucket[freq].append(num)
        
        result = []
        # Start at the highest possible frequency.
        # Move downward.
        for i in range(len(nums), 0, -1):
            result.extend(bucket[i])
            # Stop when we have k numbers.
            if len(result) >= k:
                break

        return result[:k]