> Problem: [123. 买卖股票的最佳时机 III](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iii/description/)

# 思路

> 暴力法会超时，只能用动态规划，其实暴力法还可以优化，正序遍历一次求 `0~i` 的最大利润，逆序遍历一次求 `i~n` 的最大利润，均存下来，最后两者的和就是答案

# 复杂度

- 时间复杂度: $O(n)$

- 空间复杂度: $O(1)$

# Code

```Python []

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy1 = buy2 = -prices[0]
        sell1 = sell2 = 0
        for i in range(1, n):
            buy1 = max(buy1, -prices[i])
            sell1 = max(sell1, buy1 + prices[i])
            buy2 = max(buy2, sell1 - prices[i])
            sell2 = max(sell2, buy2 + prices[i])
        return sell2


```

# Code2 暴力法 ： 美美超时，，，

```Python []
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        ans = 0
        for i in range(n):
            tempans = 0
            maxpro,minp = 0,inf
            for j in range(i):
                maxpro = max(maxpro,prices[j]-minp)
                minp = min(minp,prices[j])
            tempans += maxpro
            maxpro,minp = 0,inf
            for j in range(i,n):
                maxpro = max(maxpro,prices[j]-minp)
                minp = min(minp,prices[j])
            tempans += maxpro
            ans = max(tempans,ans)
        return ans
```

# Code3 暴力法+稍微优化下 ： 再次美美超时，，，

```Python []
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        ans = 0
        maxpro1,minp1 = 0,inf
        for i in range(n):
            maxpro1 = max(maxpro1,prices[i]-minp1)
            minp1 = min(minp1,prices[i])
            maxpro2,minp2 = 0,inf
            for j in range(i,n):
                maxpro2 = max(maxpro2,prices[j]-minp2)
                minp2 = min(minp2,prices[j])
            ans = max(maxpro1+maxpro2,ans)
        return ans
```
