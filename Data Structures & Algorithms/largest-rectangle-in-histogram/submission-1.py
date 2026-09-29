class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # (start_index, height)
        max_area = 0

        for index, height in enumerate(heights):
            # This is where the current rectangle could start.
            # It may move left when we pop taller bars.
            start_index = index

            # A shorter bar means the taller bars on the stack
            # have reached their right boundary.
            while stack and height < stack[-1][1]:
                previous_start, previous_height = stack.pop()

                # Current index is the first bar shorter than
                # previous_height, so the rectangle ends here.
                width = index - previous_start
                area = previous_height * width

                max_area = max(max_area, area)

                # The current shorter bar can extend back through
                # the space occupied by the popped bar.
                start_index = previous_start

            # Store the earliest position this height can extend from.
            stack.append((start_index, height))

        # Bars still in the stack never found a smaller bar on the right,
        # so their rectangles extend all the way to the end.
        for start_index, height in stack:
            width = len(heights) - start_index
            area = height * width
            max_area = max(max_area, area)

        return max_area