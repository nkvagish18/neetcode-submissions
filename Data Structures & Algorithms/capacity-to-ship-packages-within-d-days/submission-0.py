class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        while left < right:
            mid = (left + right) // 2
            day = 1
            load = 0
            for weight in weights:
                if load + weight > mid:
                    day += 1
                    load = 0
                load += weight
            if day <= days:
                right = mid
            else:
                left = mid + 1
        return left