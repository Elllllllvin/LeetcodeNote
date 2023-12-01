> Problem: [309. 买卖股票的最佳时机含冷冻期](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/)

[TOC]

# 思路
> 动态规划

# 复杂度
- 时间复杂度:  $O(n)$

- 空间复杂度:  $O(n)$

# Code
```Python []

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0]*3 for _ in range(n)]
# 目前持有一支股票， dp[i][0],之前买了今天不操作，或者今天刚买；
# 目前不持有任何股票，dp[i][1]，今天刚卖；
# 目前不持有任何股票，dp[i][2]，之前卖的。
        dp[0] = [-prices[0],0,0]
        for i in range(1,n):
            dp[i][0] = max(dp[i-1][0],dp[i-1][2] - prices[i])
                         #昨天就已经持有     今天刚买的
            dp[i][1] = dp[i-1][0] + prices[i]
            # 今天卖出，昨天必须持有股票
            dp[i][2] = max(dp[i-1][1],dp[i-1][2])
            #        昨天卖的，今天冷静期 或者 之前卖的，今天也没买

        return max(dp[n-1])



```
