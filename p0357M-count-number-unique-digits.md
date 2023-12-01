> Problem: [357. 统计各位数字都不同的数字个数](https://leetcode.cn/problems/count-numbers-with-unique-digits/description/)

[toc]

# 思路

排列组合啊啊啊啊
竟然没做出来55
# 复杂度

- 时间复杂度:  $O(n)$

- 空间复杂度:  $O(1)$

# Code

```Python
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 10
        res, cur = 10, 9
        for i in range(n - 1):
            cur *= 9 - i
            res += cur
        return res
```
