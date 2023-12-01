> Problem: [342. 4的幂](https://leetcode.cn/problems/power-of-four/description/)

[toc]

# 思路

> 讲述看到这一题的思路

# 解题方法

> 描述你的解题方法

# 复杂度

- 时间复杂度:

> 添加时间复杂度, 示例： $O(logn)$

- 空间复杂度:

> 添加空间复杂度, 示例： $O(1)$

# Code

```python


class Solution:

    def isPowerOfFour(self, n: int) -> bool:

        while n and n%4==0:

            n = n//4

        return n==1

```
