> Problem: [115. 不同的子序列](https://leetcode.cn/problems/distinct-subsequences/description/)

# 解题方法

> 1.自己想的递归，会超时 2.动态规划（官方题解）

# 复杂度

- 时间复杂度:

  > 添加时间复杂度, 示例： $O(n)$

- 空间复杂度:
  > 添加空间复杂度, 示例： $O(n)$

# Code1 自己想的递归，会超时 50/65

```Python []
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        self.cnt = 0
        def dfs(s,t):
            if len(t) == 0 :
                self.cnt += 1
                return

            if len(s) == 0 or len(s)<len(t):
                return

            if s[0] == t[0]:
                dfs(s[1:],t[1:])
                dfs(s[1:],t)
            else:
                dfs(s[1:],t)
        dfs(s,t)
        return self.cnt

```

# Code2 动态规划

上述表示中，s[i:]表示 s 从下标 i 到末尾的子字符串，t[j:] 表示 t 从下标 j 到末尾的子字符串。
t[n:]表示 t 为空串，空串是所有字符串的子集，因此 t[i][n] = 1

```Python []

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m,n = len(s)+1,len(t)+1
        if m<n:
            return 0
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            dp[i][n-1] = 1

        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i+1][j+1]+dp[i+1][j]
                else:
                    dp[i][j] = dp[i+1][j]

        return dp[0][0]
```
