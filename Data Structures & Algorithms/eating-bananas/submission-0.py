class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minRate, maxRate = 1, max(piles)
        result = maxRate

        while minRate <= maxRate:
            midRate = (minRate + maxRate) // 2

            totalTime = 0
            for bananas in piles:
                totalTime += math.ceil(float(bananas) / midRate)
            if totalTime <= h:
                result = midRate
                maxRate = midRate - 1
            else:
                minRate = midRate + 1
        
        return result