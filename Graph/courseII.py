#https://leetcode.com/problems/course-schedule-ii/
class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        preMap = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        cycle, visited = set(), set()
        output = []

        def dfs(crs):
            if crs in cycle:
                return False

            if crs in visited:
                return True

            cycle.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            cycle.remove(crs)
            visited.add(crs)
            output.append(crs)

            return True

        for c in range(numCourses):
            if not dfs(c):
                return []

        return output
