> Problem: [374. 猜数字大小](https://leetcode.cn/problems/guess-number-higher-or-lower/description/)

[toc]

# 思路

> 二分法搜索

# 解题方法

> 描述你的解题方法

# 复杂度

- 时间复杂度:

> 添加时间复杂度, 示例： $O(n)$

- 空间复杂度:

> 添加空间复杂度, 示例： $O(n)$

# Code

```Python3


# The guess API is already defined for you.

# @param num, your guess

# @return -1 if num is higher than the picked number

#          1 if num is lower than the picked number

#          otherwise return 0

# def guess(num: int) -> int:


class Solution:

    def guessNumber(self, n: int) -> int:

        l,r = 0,n

        while True:

            mid = (l+r)//2

            guessres = guess(mid)

            if guessres == 0:

                return mid

            elif guessres == 1:

                l = mid + 1

            else:

                r = mid - 1





```
