_Italic_> Problem: [200. 岛屿数量](https://leetcode.cn/problems/number-of-islands/description/)

# 思路

dfs！！！好久没做题直接变傻了，这道题做了 1 个小时

# Code1

```Python

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid),len(grid[0])
        res = 0
        def extention(i,j):
            if grid[i][j] == '0':
                return
            else:
                if i < m-1 and grid[i+1][j] == '1':
                    grid[i+1][j] = 'A'
                    extention(i+1,j)
                if j < n-1 and grid[i][j+1] == '1':
                    grid[i][j+1] = 'A'
                    extention(i,j+1)
                if j > 0 and grid[i][j-1] == '1':
                    grid[i][j-1] = 'A'
                    extention(i,j-1)
                if i > 0 and grid[i-1][j] == '1':
                    grid[i-1][j] = 'A'
                    extention(i-1,j)
            return
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                extention(i,j)

        return res

```
