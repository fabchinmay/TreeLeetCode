#https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:

        left, right = 1, (m * n)

        while left < right:
            mid = left + (right - left) // 2

            if self.enough(m, n, k, mid):
                right = mid
            else:
                left = mid + 1

        return left

    def enough(self, m, n, k, mid):
        count = 0

        for val in range(1, m + 1):
            add = min(mid // val, n)
            if add == 0:  # early exit
                break
            count += add
        return count >= k
