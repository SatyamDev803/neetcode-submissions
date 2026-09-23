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

                if mapping[top] == char:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0