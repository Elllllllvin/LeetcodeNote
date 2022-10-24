> Problem: [20. 有效的括号](https://leetcode.cn/problems/valid-parentheses/description/)

# 思路
> 利用栈的思想

# 解题方法
> 用一个列表模拟出栈和入栈

# 复杂度
- 时间复杂度: 
> 添加时间复杂度, 示例： $O(n)$

- 空间复杂度: 
> 添加空间复杂度, 示例： $O(n)$

# Code
```Python []

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = []
        for item in s:
            if item =='(' or item == '{' or item == '[':
                l.append(item)
            else:
                if(len(l) == 0):
                    l.append(item)
                    break
                else:
                    if item == ')':
                        if(l[-1] == '('):
                            l.pop()
                        else:
                            break
                    elif item == ']':
                        if(l[-1] == '['):
                            l.pop()
                        else:
                            break
                    elif item == '}':
                        if(l[-1] == '{'):
                            l.pop()
                        else:
                            break
        if(len(l)>0):
            return False
        else:
            return True
```
