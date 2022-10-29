#https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/submissions/
#https://leetcode.com/discuss/general-discussion/786126/python-powerful-ultimate-binary-search-template-solved-many-problems

class Solution:

    def feasible(capacity) -> bool:
        days = 1
        total = 0
        for weight in weights:
            total += weight
            if total > capacity:  # too heavy, wait for the next day
                total = weight
                days += 1
                if days > D:  # cannot ship within D days
                    return False
        return True

    def isPossible(self, weights, days, limit):
        curDay = 1
        total = weights[0]

        for weights in weights:
            total += weights

            if weights - total >= limit:
                curDay += 1
                total = weights
                if curDay == days:
                    return True

        return False

    def isFeasible(self, weights, days, limit):
        curDay = 1
        total = 0

        for weights in weights:
            total += weights

            if total > limit:
                curDay += 1

                if curDay > days:
                    return False

                total = weights

        return True

    def shipWithinDays(self, weights, days: int) -> int:
        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = left + (right - left) // 2
            if self.isFeasible(weights, days, mid):
                right = mid
            else:
                left = mid + 1

        return left

Solution = Solution()
weights=[1,2,3,4,5,6,7,8,9,10]
days=5
print(Solution.shipWithinDays(weights,days))