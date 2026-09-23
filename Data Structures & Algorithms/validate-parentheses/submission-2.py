class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        stack = []

        for char in s:
            if char in mapping:
                stack.append(char)
            else:
                if not stack:
                    return False

                top = stack[-1]

                if mapping[top] != char:
                    return False

                stack.pop()

        return not stack