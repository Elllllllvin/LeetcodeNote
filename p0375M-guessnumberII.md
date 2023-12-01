> Problem: [375. 猜数字大小 II](https://leetcode.cn/problems/guess-number-higher-or-lower-ii/description/)

[toc]

# 思路

> 动态规划dp

# 解题方法

> 具体详见代码注释

# 复杂度

- 时间复杂度: $O(n^3)$

- 空间复杂度: $O(n^2)$

# Code

```Python

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        f = [[0]*(n+1) for _ in range(n+1)]
        for i in range(n-1,0,-1): 
    #i逆序,j顺序的原因：在下面更新f[i][j]时，需要知道f[i][k-1],即需要j前面的数，因此j需要正向计算
    #                                   还需要知道f[k+1][j],需要i后面的数，因此i需要反向计算
            for j in range(i+1,n+1):
                f[i][j] = j+f[i][j-1] #我先猜是j，但是没猜准
                for k in range(i,j): #我再遍历猜是[i,j-1]中的数
                    f[i][j] = min(f[i][j],k+max(f[i][k-1],f[k+1][j]))

        return f[1][n]
```
