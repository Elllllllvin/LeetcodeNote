> Problem: [7. 整数反转](https://leetcode.cn/problems/reverse-integer/description/)

# 问题描述

给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。

如果反转后整数超过 32 位的有符号整数的范围 [−2^31, 2^31 − 1] ，就返回 0。

假设环境不允许存储 64 位整数（有符号或无符号）。

# Code 转为字符串

击败 89.7% ; 95.31%

```Python []

import math

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if(x == 0):
            return 0
        flag = 0
        strx = ''
        if (x >= 0 ):
            strx = str(x)
            strx = strx[::-1]
        else :
            strx = str(abs(x))
            strx = strx[::-1]
            flag = 1
        res = 0
        strx.lstrip('0')
        if (flag):
            res = int(strx)*-1
        else:
            res = int(strx)

        if res < -1*math.pow(2,31) or res > (math.pow(2,31)-1):
            res = 0
        return res




```
