> Problem: [172. 阶乘后的零](https://leetcode.cn/problems/factorial-trailing-zeroes/description/)

[toc]

# 思路

算阶乘后有多少个 0，就是在算因子里有多少个 10👉 就是再算因子有多少个 5（因为 2 的因子肯定比 5 多），迭代计算因子 5 的个数。

# Code

```Python
class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        while n:
            n = n//5
            res += n
        return res



```
