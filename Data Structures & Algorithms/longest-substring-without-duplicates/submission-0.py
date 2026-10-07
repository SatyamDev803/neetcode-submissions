class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastSeen = {}

        maxLength = 0
        left = 0

        for right, char in enumerate(s):
            if char in lastSeen and lastSeen[char] >= left:
                left = lastSeen[char] + 1
            
            lastSeen[char] = right

            currentLength = right - left + 1

            maxLength = max(maxLength, currentLength)

        return maxLength