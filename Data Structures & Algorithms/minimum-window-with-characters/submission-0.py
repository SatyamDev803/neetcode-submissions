class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s) < len(t):
            return ""

        requiredFreq = defaultdict(int)
        for char in t:
            requiredFreq[char] += 1

        windowFreq = defaultdict(int)
        
        required = len(requiredFreq)
        formed = 0

        left = 0
        bestStart = 0
        minLength = math.inf

        for right, char in enumerate(s):
            windowFreq[char] += 1

            if char in requiredFreq and windowFreq[char] == requiredFreq[char]:
                formed += 1
            
            while formed == required:
                currentLength = right - left + 1

                if currentLength < minLength:
                    minLength = currentLength
                    bestStart = left

                windowFreq[s[left]] -= 1

                if s[left] in requiredFreq and windowFreq[s[left]] < requiredFreq[s[left]]:
                    formed -= 1

                left += 1
        
        return "" if minLength == math.inf else s[bestStart:bestStart + minLength]

