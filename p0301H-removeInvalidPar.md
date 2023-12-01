> Problem: [301. 删除无效的括号](https://leetcode.cn/problems/remove-invalid-parentheses/description/)

[TOC]

# 思路
想的过于复杂了，，，，
先求出不合格的左括号和右括号，然后dfs进行回溯算法，是否满足条件单独判断
使用两种剪枝方法优化算法

# 复杂度
时间复杂度：$O(n \times 2^n)$ ，其中n为字符串的长度。考虑到一个字符串最多可能有2^n个子序列，每个子序列可能需要进行一次合法性检测.
空间复杂度：$O(n^2)$，其中n为字符串的长度。返回结果不计入空间复杂度，考虑到递归调用栈的深度，并且每次递归调用时需要复制字符串一次，因此空间复杂度为O(n^2)


# Code
```Python []

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        stack = []
        n = len(s)
        res = []

        Invalid_lp,Invalid_rp = 0,0
        for ch in s:
            if ch == '(':
                stack.append('(')
            elif ch == ')' :
                if stack:
                    stack.pop()
                else:
                    Invalid_rp += 1
        Invalid_lp = len(stack)



        def isValid(tmpres):
            stack = []
            for ch in tmpres:
                if ch =='(':
                    stack.append(ch)
                elif ch == ')':
                    if stack:
                        stack.pop()
                    else:
                        return False
            return len(stack) == 0

        def dfs(start,tmpres,Invalid_lp,Invalid_rp):
            if Invalid_lp == 0 and Invalid_rp == 0 and isValid(tmpres):
                res.append(tmpres)
                return
            for i in range(start,len(tmpres)):
                if i > start and tmpres[i] == tmpres[i-1]:
                    continue   # 相邻的两个一样的括号去掉哪个都一样
                if Invalid_lp + Invalid_rp > len(tmpres) - i:
                    break      # 剪枝：如果剩余的字符即使全部去掉也无法满足要求，则直接不算了
                
                if Invalid_lp > 0 and tmpres[i] == '(': #尝试去掉一个左括号
                    dfs(i,tmpres[:i]+tmpres[i+1:],Invalid_lp-1,Invalid_rp)
                if Invalid_rp > 0 and tmpres[i] == ')': #尝试去掉一个右括号
                    dfs(i,tmpres[:i]+tmpres[i+1:],Invalid_lp,Invalid_rp-1)
                
        dfs(0,s,Invalid_lp,Invalid_rp)
        
        return res

```
