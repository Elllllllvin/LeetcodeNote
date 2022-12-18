> Problem: [70. 爬楼梯](https://leetcode.cn/problems/climbing-stairs/description/)

[TOC]

# 思路

> 动态规划

# 解题方法

> 利用递归方法会重复计算过多不必要的步骤，因此使用动态规划会好一些

# Code

```Python []

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*(n+1)
        if n == 1:
            return 1
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]
```
