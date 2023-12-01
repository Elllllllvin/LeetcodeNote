> Problem: [319. 灯泡开关](https://leetcode.cn/problems/bulb-switcher/description/)

[TOC]

# 思路
数学推导：对于第k个灯泡。它被切换的次数恰好是k的约数个数，如果k有偶数个约数个数，那他就是暗，如果是奇数个，那他就是亮，而约数总是成对出现的，即只有当k是完全平方数是，他才会有奇数个约数，所以题目实际是在求[1,n]中完全平方数的个数。
# Code
```Python []

class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(math.sqrt(n+0.5))
        # 加0.5是为了保证计算出来的结果像下取整
             
```
