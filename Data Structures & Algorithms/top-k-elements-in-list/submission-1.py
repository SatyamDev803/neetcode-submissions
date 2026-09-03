class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Count frequencies.
        frequency = {}
        for num in nums:
            frequency[num] = 1 + frequency.get(num, 0)
        # 2. Put each number into a bucket based on its frequency.
        bucket = defaultdict(list)
        for num, freq in frequency.items():
            bucket[freq].append(num)
        
        result = []
        # 3. Start at the highest possible frequency.
        # 4. Move downward.
        for i in range(len(nums), 0, -1):
            result.extend(bucket[i])
            # 6. Stop when we have k numbers.
            if len(result) >= k:
                break

        return result[:k]