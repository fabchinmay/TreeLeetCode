#https://www.youtube.com/watch?v=YVnJkApO_HA&ab_channel=CodersCamp
#https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

class Solution:
    def minDays(self, bloomDay, m: int, k: int) -> int:
        left, right = 1, max(bloomDay)

        if m * k > len(bloomDay):
            return -1

        left, right = 1, max(bloomDay)
        while left < right:
            mid = left + (right - left) // 2
            print(mid,'-',self.isFeasible(bloomDay, m, k, mid))
            if self.isFeasible(bloomDay, m, k, mid):
                right = mid
            else:
                left = mid + 1
        return left

    def isFeasible(self, bloomDay, m, k, days):
        bonquets, flowers = 0, 0
        for bloom in bloomDay:
            print(bloom,'<bloom>',flowers,'<flowers>',bonquets,'<bonquets>')
            if bloom > days:
                flowers = 0
            else:
                bonquets += (flowers + 1) // k
                flowers = (flowers + 1) % k
        return bonquets >= m

Solutions = Solution()
bloomDay=[1,10,3,10,2]
m,k = 3,1

# bloomDay=[6,6,6,7,12,7,7]
# m,k = 2,3

# bloomDay = [1,10,3,10,2]
# m = 3
# k = 2

print(Solutions.minDays(bloomDay,m,k))

