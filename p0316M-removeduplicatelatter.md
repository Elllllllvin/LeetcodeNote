> Problem: [316. 去除重复字母](https://leetcode.cn/problems/remove-duplicate-letters/description/)

[TOC]

# 思路
> 单调栈问题
[这篇题解讲得特别好](https://leetcode.cn/problems/remove-duplicate-letters/solutions/290200/yi-zhao-chi-bian-li-kou-si-dao-ti-ma-ma-zai-ye-b-4/)

# 解题方法
> 描述你的解题方法

# 复杂度
- 时间复杂度:  $O(n^2)$

- 空间复杂度:  $O(n)$

# Code
```Python []

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        remain_counter = collections.Counter(s)

        for c in s:
            if c not in stack:
                while stack and c < stack[-1] and remain_counter[stack[-1]] > 0:
                    stack.pop()
                stack.append(c)
            remain_counter[c]-=1
        
        return ''.join(stack)
            

```
