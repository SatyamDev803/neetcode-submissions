class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mapS1 = [0] * 26
        mapS2 = [0] * 26

        for char in s1:
            index = ord(char) - ord('a')
            mapS1[index] += 1

        for i in range(len(s1)):
            # Missing
            if len(s1) > len(s2):
                return False
            index = ord(s2[i]) - ord('a')
            mapS2[index] += 1

        left = 0
        right = len(s1) - 1

        while right < len(s2):
            if mapS1 == mapS2:
                return True

            # Missing
            if right == len(s2) - 1:
                break

            mapS2[ord(s2[left]) - ord('a')] -= 1
            left += 1
            right += 1
            mapS2[ord(s2[right]) - ord('a')] += 1
        
        return False