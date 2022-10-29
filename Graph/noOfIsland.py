class Solution:
    def numIslands(self, grid) -> int:
        if not grid or not grid[0]:
            return 0

        islands = 0
        visit = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if (r not in range(rows) or
                    c not in range(cols) or
                    grid[r][c] == "0" or
                    (r, c) in visit):
                return

            visit.add((r, c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    islands += 1
                    dfs(r, c)
        return islands

    def numIslands2(self, grid):
        numOfIsland=0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c]=='1':
                    numOfIsland+=self.bfs2(grid,r,c)

        return numOfIsland

    def bfs2(self,grid,r,c):
        #if r<0 or r>=len(grid) or c<0 or c >=len(grid[r]) or grid[r][c]=='0':
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[r]) or grid[r][c] == '0':
            return 0

        grid[r][c]='0'
        self.bfs2(grid,r+1,c)
        self.bfs2(grid,r-1, c)
        self.bfs2(grid, r, c + 1)
        self.bfs2(grid, r, c - 1)


        return 1




        return 1




grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

Solution = Solution()
print(Solution.numIslands(grid))

print(Solution.numIslands2(grid))