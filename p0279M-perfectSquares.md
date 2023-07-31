> Problem: [279. 完全平方数](https://leetcode.cn/problems/perfect-squares/description/)

[TOC]

# 思路
> 1.动态规划！！基本思想`dp[i] = dp[i - j*j]+1`,但这不一定是最小的，因此还要遍历平方比i小的所有j！！完全背包问题！！

# 解题方法
> 描述你的解题方法


# Code1 动态规划
时间：$O(n*\sqrt{n})$  空间：$O(n)$
```Python []

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0]*(n+1)        
        for i in range(1,n+1):
            minn = i #最坏也就是j个1加起来
            j = 1
            while j*j <=i :
                minn = min(minn,dp[i-j*j])
                j += 1
            dp[i] = minn + 1
        return dp[-1]
```
