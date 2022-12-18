> Problem: [44. 通配符匹配](https://leetcode.cn/problems/wildcard-matching/description/)

# 思路

> 动态规划！！！画状态图+设置边界条件！！

# 解题方法

> 设置 dp[m+1][n+1],其中 dp[i-1][j-1]表示 s 的前 i 个字符和 p 的前 j 个字符的匹配关系

- 程序流程图
  - `如果p[j-1]==字母 : s[i]==p[j] -> dp[i][j] = dp[i-1][j-1]`
  - `如果p[j-1]=='*' : dp[i][j] = dp[i][j-1] `('\*'号匹配空串)`or dp[i-1][j]` (星号匹配任意字符)
  - `如果p[j-1]=='?' : dp[i][j] = dp[i-1][j-1]`

# 复杂度

- 时间复杂度:

  > $O(mn)$

- 空间复杂度:
  > $O(mn)$

# Code

```Python []

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m,n = len(s),len(p)
        dp = [[False]*(n+1) for i in range(m+1)]
        dp[0][0] = True
        for i in range(1,n+1):
            if p[i-1] == '*':
                dp[0][i] = True
            else:
                break

        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[i-1] == p[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]

        return dp[m][n]




```
