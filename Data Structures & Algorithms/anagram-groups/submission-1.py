class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for char in s:
                # character → index
                index = ord(char) - ord("a")
                # increment count
                count[index] += 1

            key = tuple(count)
            # put s into the group identified by key
            res[key].append(s)
            
        return list(res.values())