> Problem: [76. 最小覆盖子串](https://leetcode.cn/problems/minimum-window-substring/description/)

# 思路

> 不会优化。。。。做的想死。。

# Code

```Python []

import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ''
        hashmap = collections.defaultdict(int)
        for letter in t:
            hashmap[letter] += 1
        def satisfied(temp):
            for item in hashmap.keys():
                if temp[item] < hashmap[item]:
                    return False
            return True

        temphash = collections.defaultdict(int)
        l,r = 0,0
        res = s
        flag = False

        while r < len(s):
            if s[r] not in hashmap.keys():
                r += 1
            else:
                temphash[s[r]] += 1
                r += 1
            while satisfied(temphash):
                if len(res) >= r-l  :
                    res = s[l:r]
                    flag = True
                if s[l] in hashmap.keys():
                    temphash[s[l]] -= 1
                l += 1

        if flag == False:
            res = ''
        return res













```
