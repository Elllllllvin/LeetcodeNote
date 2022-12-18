> Problem: [139. 单词拆分](https://leetcode.cn/problems/word-break/description/)

# 思路

> 动态规划！！

# Code

- 时间复杂度: $O(n^2)$
- 空间复杂度: $O(n)$

```Python []

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False]*(n+1)
        dp[0] = True
        for i in range(n):
            for j in range(i+1,n+1):
                if(dp[i] and (s[i:j] in wordDict)):
                    dp[j]=True
        return dp[-1]

```
