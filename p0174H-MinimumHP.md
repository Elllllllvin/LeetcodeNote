_Italic_> Problem: [174. 地下城游戏](https://leetcode.cn/problems/dungeon-game/description/)

# 思路

> 尼玛做好久没做出来，，，，，从后往前的 dp 动态规划。。。。。。。。

# Code 动态规划

```Python
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n, m = len(dungeon), len(dungeon[0])
        BIG = 10**9
        dp = [[BIG] * (m + 1) for _ in range(n + 1)]
        dp[n][m - 1] = dp[n - 1][m] = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                minn = min(dp[i + 1][j], dp[i][j + 1])
                dp[i][j] = max(minn - dungeon[i][j], 1)
        print(dp)
        return dp[0][0]

```
