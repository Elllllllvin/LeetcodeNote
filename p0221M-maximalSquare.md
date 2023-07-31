> Problem: [221. 最大正方形](https://leetcode.cn/problems/maximal-square/description/)

[TOC]

# 思路
> 动态规划，，，，，md没做出来，，，，，

# 复杂度
- 时间复杂度: 
> 添加时间复杂度, 示例： $O(n)$

- 空间复杂度: 
> 添加空间复杂度, 示例： $O(n)$

# Code
```Python []

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        #动态规划
        m,n = len(matrix),len(matrix[0])
        dp = [[0]*(n+1) for i in range(m+1)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    dp[i+1][j+1] = min(dp[i][j], dp[i+1][j], dp[i][j+1]) + 1
                    ans = max(ans, dp[i+1][j+1])
        return ans**2


```
