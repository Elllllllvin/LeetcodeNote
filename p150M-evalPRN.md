> Problem: [150. 逆波兰表达式求值](https://leetcode.cn/problems/evaluate-reverse-polish-notation/description/)

# 思路

> 后缀表达式计算

# 复杂度

- 时间复杂度: $O(n)$
- 空间复杂度: $O(n)$

# Code

```Python []

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            token = tokens[i]
            if token.isdigit() or len(token)>1 :
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                x = 0
                if token == '+':
                    x = a+b
                elif token == '-':
                    x = a-b
                elif token == '*':
                    x = a*b
                elif token == '/':
                    x = int(a/b)
                stack.append(x)
        return stack[-1]
```
