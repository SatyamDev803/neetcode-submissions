class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []

        for index, pos in enumerate(position):
            cars.append((pos, speed[index]))

        cars.sort(reverse=True)

        fleet_count = 0
        fleet_time = 0

        for position, speed in cars:
            arrival_time = (target - position) / speed

            if arrival_time > fleet_time:
                fleet_count += 1
                fleet_time = arrival_time

        return fleet_count