> Problem: [71. 简化路径](https://leetcode.cn/problems/simplify-path/description/)

# 思路

> 栈的方法

# 解题方法

> 栈的方法

# Code

```Python []
class Solution:
    def simplifyPath(self, path: str) -> str:
        l = path.split('/')
        print(l)
        stack = []
        for item in l:
            if item == '':
                continue
            elif item == '.':
                continue
            elif item == '..':
                if len(stack)>0:
                    stack.pop()
                else:
                    continue
            else:
                stack.append(item)
        res = ''
        for item in stack:
            res = res + '/'+item
        if res == '':
            res = '/'
        return res
```
