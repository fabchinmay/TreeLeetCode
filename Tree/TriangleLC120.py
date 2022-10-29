#https://leetcode.com/problems/triangle/
#https://www.youtube.com/watch?v=OM1MTokvxs4&list=PLot-Xpze53ldg4pN6PfzoJY7KsKcxF1jg&index=7&ab_channel=NeetCode
def minTotal(triangle):
    dp=[0] * (len(triangle)+1)

    for row in triangle[::-1]:
        for i,n in enumerate(row):
            dp[i]= n+min(dp[i],dp[i+1])

    return dp[0]


triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]

print(minTotal(triangle))