_Italic_> Problem: [191. 位 1 的距离](https://leetcode.cn/problems/reverse-bits/description/)

# 思路

循环找，竟然超过 99%！！！

# Code1

```Python
class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n!=0 :
            cnt += n&1
            n >>= 1
        return cnt
```
