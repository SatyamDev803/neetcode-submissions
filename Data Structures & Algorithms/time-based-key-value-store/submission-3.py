class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        if self.store[key][0][0] > timestamp:
            return ""
        
        left = 0

        right = len(self.store[key]) - 1

        while left < right:
            mid = (left + right + 1) // 2

            if self.store[key][mid][0] <= timestamp:
                left = mid
            else:
                right = mid - 1

        return self.store[key][left][1]
