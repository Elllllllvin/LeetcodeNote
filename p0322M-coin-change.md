> Problem: [322. 零钱兑换](https://leetcode.cn/problems/coin-change/description/)

[toc]

# 思路

> 讲述看到这一题的思路

# 解题方法

> 描述你的解题方法

# 复杂度

- 时间复杂度: O(S*n)
- 空间复杂度：O(S)

# Code

```Python

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [inf]*(amount+1)
        dp[0] = 0
        for coin in coins:
            for x in range(coin,amount+1):
                dp[x] = min(dp[x],dp[x-coin]+1)

        return dp[amount] if dp[amount]!= inf else -1
      
```