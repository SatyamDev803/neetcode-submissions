class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for index, height in enumerate(heights):
            start_index = index
            while stack and height < stack[-1][1]:
                previous_start, previous_height = stack.pop()
                width = index - previous_start
                area = previous_height * width
                max_area = max(max_area, area)
                start_index = previous_start
            stack.append((start_index, height))

        for start_index, height in stack:
            width = len(heights) - start_index
            area = height * width
            max_area = max(max_area, area)

        return max_area