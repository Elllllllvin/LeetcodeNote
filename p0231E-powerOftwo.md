> Problem: [231. 2 的幂](https://leetcode.cn/problems/power-of-two/description/)

[TOC]

# 思路
> 没啥好说的

# 解题方法
> 描述你的解题方法

# 复杂度
- 时间复杂度: 
> 添加时间复杂度, 示例： $O(n)$

- 空间复杂度: 
> 添加空间复杂度, 示例： $O(n)$

# Code
```Python3 []

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 0:
            return False
        binN = str(bin(n))
        if binN.count('1') == 1:
            return True
        else:
            return False
```
