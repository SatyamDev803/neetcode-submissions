class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for string in strs:
            key = tuple(sorted(string))
            if key in group:
                group[key].append(string)
            else:
                group[key] = [string]

        return list(group.values())