> Problem: [263. 丑数](https://leetcode.cn/problems/ugly-number/description/)

[TOC]

# 复杂度
- 时间复杂度:  $O(logn)$

- 空间复杂度:  $O(n)$

# Code
```Python []

class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False
        while n%2 == 0:
            n = n//2
        while n%3 == 0:
            n = n//3
        while n%5 == 0:
            n = n//5
        if n == 1:
            return True
        else:
            return False
                

```
