> Problem: [224. 基本计算器](https://leetcode.cn/problems/basic-calculator/description/)

[TOC]

# 思路
> 利用堆栈的思想做！！！！！

# 复杂度
- 时间复杂度: 
> 添加时间复杂度, 示例： $O(n)$

- 空间复杂度: 
> 添加空间复杂度, 示例： $O(n)$

# Code
```Python []

class Solution:
    def calculate(self, s: str) -> int:
        res,num,sign = 0,0,1
        stack = []
        for c in s:
            if c.isdigit():
                num = num*10+int(c)
            elif c == '+':
                res += sign * num
                num = 0
                sign = 1
            elif c == '-':
                res += sign * num
                num = 0
                sign = -1
            elif c == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif c == ')':
                res += sign *num
                num = 0
                res *= stack.pop()
                res += stack.pop()
        res += sign * num
        return res
```
