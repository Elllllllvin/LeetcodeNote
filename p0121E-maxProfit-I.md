> Problem: [121. 买卖股票的最佳时机](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/description/)

# 思路

> 这么简单竟然没做出来。。。。

# Code1 暴力法：直接美美超时

# 复杂度

- 时间复杂度: $O(n^2)$

- 空间复杂度: $O(1)$

```Python []
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPrice = 0
        n = len(prices)
        for i in range(n):
            for j in range(i+1,n):
                if prices[j]-prices[i] > maxPrice:
                    maxPrice =  prices[j]-prices[i]
        return maxPrice
```

# Code2 一次遍历

# 复杂度

- 时间复杂度: $O(n)$

- 空间复杂度: $O(1)$

```Python []

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0]*len(prices)
        maxProfit = 0
        minPrice = inf
        for i in range(len(prices)):
            maxProfit = max(prices[i]-minPrice,maxProfit)
            minPrice = min(prices[i],minPrice)
        return maxProfit
```
