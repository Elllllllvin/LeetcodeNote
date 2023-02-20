_Italic_> Problem: [205. 同构数](https://leetcode.cn/problems/isomorphic-strings/solutions/)

# 思路

1.双向哈希表

# Code1

时间复杂度：o(n)

```Python
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic1,dic2 = {},{}
        for i in range(len(s)):
            dic1[s[i]] = t[i]
            dic2[t[i]] = s[i]
        res1,res2 = '',''
        for i in range(len(s)):
            res1 += dic1[s[i]]
            res2 += dic2[t[i]]

        return res1 == t and res2 == s
```
