> Problem: [345. 反转字符串中的元音字母](https://leetcode.cn/problems/reverse-vowels-of-a-string/description/)

[toc]

# 复杂度

- 时间复杂度: $O(n)$

- 空间复杂度: $O(n)$

# Code

```Python

class Solution:
    def reverseVowels(self, s: str) -> str:
        n = len(s)
        l,r = 0,n-1
        res =['']*n
        alphabet = ['a','A','e','E','i','I','o','O','u','U']
        while l<=r:
            while s[l] not in alphabet and l<r:
                res[l] = s[l]
                l+=1
            while s[r] not in alphabet and l<r:
                res[r] = s[r]
                r-=1
            if l>r:
                break
            res[l],res[r] = s[r],s[l]
            l+=1
            r-=1
        return ''.join(res)

```
