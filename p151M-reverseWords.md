> Problem: [151. 反转字符串中的单词](https://leetcode.cn/problems/reverse-words-in-a-string/description/)

# 思路

> 利用 python 特性

# 复杂度

- 时间复杂度: $O(n)$
- 空间复杂度: $O(n)$

# Code

```Python []

class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.strip().split(' ')
        s = ''
        for i in range(len(l)-1,-1,-1):
            if l[i]!='':
                s+=l[i]+' '
        return s[:-1]
```
