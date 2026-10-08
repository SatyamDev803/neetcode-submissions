class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        left = 0
        maxFrequency = 0
        result = 0

        for right, char in enumerate(s):
            count[char] += 1
            maxFrequency = max(maxFrequency, count[char])

            windowLength = right - left + 1
            replacement = windowLength - maxFrequency

            while replacement > k:
                count[s[left]] -= 1
                left += 1
                windowLength -= 1
                replacement = windowLength - maxFrequency

            result = max(result, windowLength)

        return result