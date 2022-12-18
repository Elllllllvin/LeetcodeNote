> Problem: [120. 三角形最小路径和](https://leetcode.cn/problems/triangle/description/)

# 思路

> 1.动态规划+二维数组 2.动态规划+一维数组（优化）

# Code1 动态规划+二维数组

- 时间复杂度: $O(n^2)$

- 空间复杂度: $O(n^2)$

```Python []

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m,n = len(triangle),len(triangle[-1])
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = triangle[0][0]
        for i in range(1,m):
            for j in range(i+1):
                if j == 0:
                    dp[i][j] = triangle[i][j]+dp[i-1][j]
                elif j == i:
                    dp[i][j] = triangle[i][j]+dp[i-1][j-1]
                else:
                    dp[i][j] = triangle[i][j] + min(dp[i-1][j],dp[i-1][j-1])

        return min(dp[-1])


```

# Code2 （优化）动态规划+一维数组

```Python []

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m,n = len(triangle),len(triangle[-1])
        dp = [0]*n
        dp[0] = triangle[0][0]
        for i in range(1,m):
            pre = dp[:]
            for j in range(i+1):
                if j == 0:
                    dp[j] = triangle[i][j]+pre[j]
                elif j == i:
                    dp[j] = triangle[i][j]+pre[j-1]
                else:
                    dp[j] = triangle[i][j] + min(pre[j],pre[j-1])
            print(dp)

        return min(dp)


```
