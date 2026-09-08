class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        changes = defaultdict(int)

        for passengers, start, end in trips:
            changes[start] += passengers
            changes[end] -= passengers

        current = 0

        for location in sorted(changes):
            current += changes[location]

            if current > capacity:
                return False

        return True