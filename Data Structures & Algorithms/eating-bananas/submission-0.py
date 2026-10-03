class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2

            total_hours = 0

            for pile in piles:
                if pile % mid == 0:
                    hours = pile // mid
                else:
                    hours = (pile // mid) + 1

                total_hours += hours

            if total_hours <= h:
                right = mid
            else:
                left = mid + 1

        return left