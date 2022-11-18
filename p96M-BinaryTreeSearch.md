> Problem: [96. 不同的二叉搜索树](https://leetcode.cn/problems/unique-binary-search-trees/description/)

# 思路

> 动态规划！

# Code

```Python []

class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[0],dp[1] = 1 , 1
        for i in range(2,n+1):
            for j in range(i):
                dp[i]+=dp[j]*dp[i-1-j]

        return dp[n]

```
