> Problem: [64. 最小路径和](https://leetcode.cn/problems/minimum-path-sum/description/)

[TOC]

# 思路

> 简单的动态规划

# Code

```Python []

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        for i in range(1,m):
            grid[i][0] = grid[i-1][0] + grid[i][0]
        for i in range(1,n):
            grid[0][i] = grid[0][i-1] + grid[0][i]
        for i in range(1,m):
            for j in range(1,n):
                grid[i][j] = grid[i][j]+min(grid[i][j-1],grid[i-1][j])

        return grid[m-1][n-1]





```
