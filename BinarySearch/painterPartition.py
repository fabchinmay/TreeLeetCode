#https://www.interviewbit.com/old/problems/painters-partition-problem/
#https://www.youtube.com/watch?v=wwEF9x5Mgt0&ab_channel=nETSETOS
class Solution:
    # @param A : integer : No of Painters
    # @param B : integer : Units of Time
    # @param C : list of integers
    # @return an integer
    def paint(self, A, B, C):
        right = sum(C)
        left = max(C)

        def isFeasible(A,C,limit):
            painters=1
            totalBrush=0

            for C in C:
                totalBrush+=C
                if totalBrush>=limit:
                    painters+=1
                    if painters>A:
                        return False
                    totalBrush=C
            return True

        while left < right:
            mid = left + (right - left) // 2
            painter = 1
            board = 0

            for brush in C:
                board += brush

                if board > mid:
                    painter += 1
                    board = brush

            #if painter <= A:
            if  isFeasible(A, C, mid):
                right = mid
            else:
                left = mid + 1

        return (left * B) % 10000003
        #return left

Solution = Solution()
A = 2
B = 5
C = [1, 10]


# A = 10
# B = 1
# C = [1, 8,11,3]
print(Solution.paint(A,B,C))



