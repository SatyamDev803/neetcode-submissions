class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {"(": ")", "[": "]", "{": "}"}

        stack = []

        for char in s:
            if char in mapping:
                stack.append(char)

            else:
                if len(stack) == 0:
                    return False

                top = stack[-1]

                if mapping[top] != char:
                    return False

                stack.pop()

        if len(stack) == 0:
            return True
        else:
            return False
