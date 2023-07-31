> Problem: [292. Nim 游戏](https://leetcode.cn/problems/nim-game/description/)

[TOC]

# 思路
n是四的倍数时，必输

# Code
```Python []

class Solution:
    def canWinNim(self, n: int) -> bool:
        return not n%4 == 0
```
