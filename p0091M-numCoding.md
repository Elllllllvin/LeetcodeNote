> Problem: [91. 解码方法](https://leetcode.cn/problems/decode-ways/description/)

# 思路

> 真的醉了，动态规划的题我用回溯，回溯的题我用动态规划。。。。。。

# Code1 动态规划

```Python []

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        f = [1]+[0]*len(s)
        for i in range(1,n+1):
            if s[i-1] != '0':
                f[i] += f[i-1]
            if i>1 and s[i-2] != '0' and int(s[i-2:i])<=26:
                f[i] += f[i-2]

        return f[n]

```

# Code2 自己用的 dfs 普通的能过，长的会超时。。。

```Python []
class Solution:
    def numDecodings(self, s: str) -> int:
        res = []
        def dfs(s):
            # print(s)
            n = len(s)
            if n == 0:
                res.append(1)
                return
            if n == 1:
                if s[0] !='0':
                    res.append(1)
                    return
                else:
                    return
            if s[0]=='0':
                return
            elif s[1]=='0' and s[0] in ['1','2']:
                dfs(s[2:])
            else:
                if 1<= int(s[0:2]) <= 26:
                    dfs(s[1:])
                    dfs(s[2:])
                else:
                    dfs(s[1:])
        dfs(s)
        return len(res)
```
