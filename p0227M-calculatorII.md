> Problem: [227. 基本计算器 II](https://leetcode.cn/problems/basic-calculator-ii/description/)

[TOC]

# 思路
> 栈的思想

# 复杂度
- 时间复杂度: 
> 添加时间复杂度, 示例： $O(n)$

- 空间复杂度: 
> 添加空间复杂度, 示例： $O(n)$

# Code
```Python []

class Solution:
    def calculate(self, s: str) -> int:
        stack = []

        presign = '+'
        temp = 0
        
        for i in range(len(s)):
            if s[i] != ' ' and s[i].isdigit():
                temp = temp * 10 + ord(s[i]) - ord('0')
            if i == len(s)-1 or s[i] in ['+','-','*','/']:
                if presign == '+':
                    stack.append(temp)
                elif presign == '-':
                    stack.append(-temp)
                elif presign == '*':
                    stack.append(stack.pop() * temp)
                elif presign == '/':
                    stack.append(int(stack.pop() / temp))
                presign = s[i]
                temp = 0
        return sum(stack)



```
