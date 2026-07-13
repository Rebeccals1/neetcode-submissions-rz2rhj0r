class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)  # our Rates
        results = right

        while left <= right:
            mid = (left + right) // 2

            totalTime = 0
            for bananas in piles:
                totalTime += math.ceil(float(bananas) / mid)
            if totalTime <= h:
                results = mid
                right = mid - 1
            else:
                left = mid + 1

        return results
            


