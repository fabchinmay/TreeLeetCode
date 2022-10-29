#Koko banana Problem
#https://www.youtube.com/watch?v=LzZFUTWE55c&ab_channel=Pepcoding
# TC - O(n⋅logm) SC - O(1)
import math
class Solution:
    def isFeasible(self, piles, hour, speed):
        totalHours = 0
        for pile in piles:
            totalHours += math.ceil(pile / speed)
            # totalHours+=math.ceil((pile-1)/speed+1)
        return totalHours <= hour

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left < right:
            mid = left + (right - left) // 2

            if self.isFeasible(piles, h, mid):
                right = mid
            else:
                left = mid + 1

        return left




















