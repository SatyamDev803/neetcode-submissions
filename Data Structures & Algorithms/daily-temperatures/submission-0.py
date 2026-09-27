class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for day, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][1]:
                previous_day, _ = stack.pop()
                result[previous_day] = day - previous_day

            stack.append((day, temperature))

        return result