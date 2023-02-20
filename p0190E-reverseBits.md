_Italic_> Problem: [190. 颠倒二进制位](https://leetcode.cn/problems/reverse-bits/description/)

# 思路

法 1：一位一位的变
法 2：位运算分治

# Code1: 一位一位的变

```Python
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(31):
            res += n & 1
            res <<= 1
            n >>= 1
        res += n & 1
        return res
```

# Code2：位运算分治

```Python
class Solution:
    def reverseBits(self, n: int) -> int:
        n = (n >> 16) | (n << 16)
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
        return n
```
