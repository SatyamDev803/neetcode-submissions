class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # (start_index, height)
        max_area = 0

        # The final 0 forces all remaining bars to be processed.
        for index, height in enumerate(heights + [0]):
            start_index = index

            # Pop every taller bar because its rectangle ends here.
            while stack and height < stack[-1][1]:
                previous_start, previous_height = stack.pop()

                width = index - previous_start
                area = previous_height * width

                max_area = max(max_area, area)

                # The shorter bar can extend into the popped bar's range.
                start_index = previous_start

            # Save where this height can begin extending from.
            stack.append((start_index, height))

        return max_area