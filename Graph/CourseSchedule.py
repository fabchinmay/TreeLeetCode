#https://leetcode.com/problems/course-schedule/submissions/
class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        # dfs
        preMap = {i: [] for i in range(numCourses)}

        # map each course to : prereq list
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visiting = set()

        def dfs(crs):
            print(visiting,"-",preMap)
            if crs in visiting:
                return False
            if preMap[crs] == []:
                return True

            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    print(pre)
                    return False
            visiting.remove(crs)
            preMap[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c): return False
        return True


numCourses=5
prerequisites=[[0,1],[0,2],[1,3],[1,4],[3,4]]#[[0,1],[1,2],[2,0]] #False
    #[[0,1],[0,2],[1,3],[1,4],[3,4],[4,1]] #True#[[0,1],[1,[2,3]],[2,4],[3,5]]

Solution = Solution()
print(Solution.canFinish(numCourses,prerequisites))
