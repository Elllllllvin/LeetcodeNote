> Problem: [122. 买卖股票的最佳时机 II](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/description/)

[TOC]

# 思路

> 简单的动态规划

# Code

```Python []
   # *** 推理逻辑：
   # 1. 在任意位置，只有卖掉股票才可能盈利: sell一个值就够了
   # 2. 如果以前位置卖了比拿到今天更赚（就是股价今天跌了），就用以前的: sell = max(sell, sell + diffVal)
   # 3. 卖了之后，不买不卖，还是用以前的总盈利: 啥也不做
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0]*n
        for i in range(1,n):
            if prices[i]>prices[i-1]:
                dp[i] = dp[i-1]+prices[i]-prices[i-1]
            else:
                dp[i] = dp[i-1]
        return dp[n-1]

```
