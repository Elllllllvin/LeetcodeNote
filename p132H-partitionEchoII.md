> Problem: [132. 分割回文串 II](https://leetcode.cn/problems/palindrome-partitioning-ii/description/)

# 思路

> 好难，，，，类似的题看到好几次还是做不出。。。。。

# 解题方法

> 动态规划
> `g[i][j]`表示 s[i...j]是回文字符串，

- 当 `i>j` 时，表示空字符串，一定是回文串，`g[i][j]=True`
- 当 `i=j` 时，表示一个字符，一定是回文串，`g[i][j]=True`
- 当 `i<j` 时，当`s[i]==s[j] and g[i+1][j-1] == True`,`g[i][j]=True`

# Code1 动态规划

- 时间复杂度: $O(n^2)$
- 空间复杂度: $O(n^2)$

```Python []

class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        g = [[True] * n for _ in range(n)]

        # 更新动态规划
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                g[i][j] = (s[i] == s[j]) and g[i + 1][j - 1]

        # 计算最小分割次数
        f = [float("inf")] * n
        for i in range(n):
            if g[0][i]: #从s[0到i]是回文字符串
                f[i] = 0 #分割次数
            else:       #若s[0到i]不是回文字符串，则寻找0~i之间的最小分割次数
                for j in range(i):
                    if g[j + 1][i]:
                        f[i] = min(f[i], f[j] + 1) #更新最小分割次数

        return f[n - 1]
```

# Code2 暴力递归：p131 改进，美美超时，，，，，，

```Python []
class Solution:
    def minCut(self, s: str) -> int:
        res = []
        self.mincut = inf
        def dfs(temps,path,cnt):
            if cnt >= self.mincut and len(temps)!=0:
                return
            if len(temps) == 0:
                self.mincut = cnt-1
            for i in range(1,len(temps)+1):
                x = temps[:i]
                if x == x[::-1]:
                    dfs(temps[i:],path+[temps[:i]],cnt+1)
        dfs(s,[],0)
        return self.mincut
```
