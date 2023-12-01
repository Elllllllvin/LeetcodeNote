> Problem: [371. 两整数之和](https://leetcode.cn/problems/sum-of-two-integers/description/)

[toc]

# 思路

> 位运算


# Code

```Python


MASK1 = 4294967296  # 2^32

MASK2 = 2147483648  # 2^31

MASK3 = 2147483647  # 2^31-1


class Solution:

    def getSum(self, a: int, b: int) -> int:

        x = 0xffffffff

        a, b = a & x, b & x

        # 循环，当进位为 0 时跳出

        while b != 0:

            # a, b = 非进位和, 进位

            a, b = (a ^ b), (a & b) << 1 & x

        return a if a <= 0x7fffffff else ~(a ^ x)


```
