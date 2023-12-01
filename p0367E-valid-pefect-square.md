> Problem: [367. 有效的完全平方数](https://leetcode.cn/problems/valid-perfect-square/description/)

[toc]

# 思路

> 讲述看到这一题的思路

# 解题方法

> 描述你的解题方法

# 复杂度

- 时间复杂度: $O(logn)$

- 空间复杂度: $O(1)$

# Code

```Python


class Solution:

    def isPerfectSquare(self, num: int) -> bool:

        if num == 1:

            return True

        l,r = 1,num

        while l<=r:

            mid = (l+r)//2

            mid_square = mid*mid

            if mid_square == num:

                return True

            elif mid_square > num:

                r = mid-1

            elif mid_square < num:

                l = mid+1

        return False


```
