class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        
        for s in strs:
            encoded_string += str(len(s)) + "#" + s

        return encoded_string
        
    def decode(self, s: str) -> List[str]:
        # 5   #   H   e   l   l   o   5   #   W   o   r   l   d
        # 0   1   2   3   4   5   6   7   8   9  10  11  12  13

        result = []
        i = 0
        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])
            start = j + 1
            end = start + length

            decoded_string = s[start:end]

            result.append(decoded_string)
            i = end

        return result




