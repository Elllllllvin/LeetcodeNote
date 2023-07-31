> Problem: [264. 丑数 II](https://leetcode.cn/problems/ugly-number-ii/description/)

[TOC]

# 思路
> 动态规划


# 复杂度
- 时间复杂度:  $O(n)$

- 空间复杂度:  $O(n)$

# Code
```Python []

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n < 0:
            return 0
        dp = [1]*n
        i2,i3,i5 = 0,0,0
        for i in range(1,n):
            dp[i] = min( 2*dp[i2] , 3*dp[i3] , 5*dp[i5] )
            if dp[i] == 2*dp[i2]:
                i2 += 1
            if dp[i] == 3*dp[i3]:
                i3 += 1
            if dp[i] == 5*dp[i5]:
                i5 += 1
        
        return dp[n-1]

```
