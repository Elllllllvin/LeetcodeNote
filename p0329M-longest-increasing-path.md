> Problem: [329. 矩阵中的最长递增路径](https://leetcode.cn/problems/longest-increasing-path-in-a-matrix/description/)

[toc]

# 思路

> 记忆化深度优先所有，当dfs要重复计算的时候，用记忆化递归搜索，会容易很多！！！

# 解题方法

> 描述你的解题方法

# 复杂度

- 时间复杂度: $O(mn)$

- 空间复杂度: $O(mn)$

# Code

```Python


  class Solution:

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        if not matrix:

            return 0

        DIRS = [(-1,0),(1,0),(0,1),(0,-1)]

        m,n = len(matrix),len(matrix[0])


        @lru_cache(None)

        def dfs(row,col):

            best = 1

            for dx,dy in DIRS:

                newRow ,newCol = row + dx , col + dy

                if 0 <= newRow < m and 0 <= newCol < n and matrix[newRow][newCol] > matrix[row][col]:

                    best = max(best,dfs(newRow,newCol) + 1)

            return best

        res = 0

        for i in range(m):

            for j in range(n):

                res = max(res,dfs(i,j))


        return res



```
