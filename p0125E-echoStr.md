> Problem: [125. 验证回文串](https://leetcode.cn/problems/valid-palindrome/description/)

# 思路

> 回文字符串 + 删除非法字符

# Code

```Python []

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = list(s)
        for i in range(len(s)):
            if s[i].isalnum():
                continue
            else:
                s[i] = ""
        s = ''.join(s)

        return s == s[::-1]

```
