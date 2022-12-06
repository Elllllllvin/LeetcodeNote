> Problem: [140. 单词拆分 II](https://leetcode.cn/problems/word-break-ii/description/)

# 思路

> dfs+回溯

# Code

```Python []

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        res = []
        def dfs(s,path):
            if not s:
                res.append(path[:-1])
                return
            for i in range(len(s)+1):
                if s[:i] in wordDict:
                    dfs(s[i:],path+s[:i]+' ')
        dfs(s,'')
        return res
```
