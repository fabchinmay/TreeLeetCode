#https://leetcode.com/problems/unique-binary-search-trees/submissions/
#https://www.youtube.com/watch?v=Ox0TenN3Zpg&list=PLot-Xpze53ldg4pN6PfzoJY7KsKcxF1jg&index=9&ab_channel=NeetCode
#TC O(n^2) SC O(n)
def noOfUniqueBST(n):
    numTree = [1] * (n+1)

    for node in range(2,n+1):
        total=0
        for root in range(1,node+1):
            left = root-1
            right = node - root

            total += numTree[left]*numTree[right]

        numTree[node]=total

    return numTree[n]

print(noOfUniqueBST(3))