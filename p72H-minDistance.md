> Problem: [72. 编辑距离](https://leetcode.cn/problems/edit-distance/description/)

# 思路

> 大厂面试题！重要！！动态规划！！！

# 解题方法

> 题目要求：给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数 。

要将 word1 转化成 word2，使用动态规划的思想，例如：对于‘horse’和‘ros’，

- 如果知道‘horse’到‘ro’的距离 x，则 ans = x + 1 (转化为‘ro’后面加一个 s 即可得到答案)
- 如果知道‘hors’到‘ros’的距离 y，则 ans = y + 1 (‘horse’转化为‘rose’再删除一个‘e’，即可得到答案)
- 如果知道 ‘hors’到‘ro’的距离 z，则进一步判断：word1 和 word2 最后一位一样吗？
  - 一样的话转换到‘ro’不用再换了，则 ans = z
  - 不一样的话，还需将最后一位 e 修改为 s，则 ans = z + 1

**最终答案去上述三种情况的最小值**
使用 dp[ ][ ]动态规划，其中`dp[i][j]`表示`word1[:i+1]`转化到`word2[:j+1]`所需最小操作数

# 复杂度

- 时间复杂度: $O(m*n)$

- 空间复杂度: $O(m*n)$

# Code

```Python []

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n = len(word1),len(word2)
        # initialize
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = i
        for i in range(n+1):
            dp[0][i] = i
        #update
        for i in range(1,m+1):
            for j in range(1,n+1):
                left = dp[i][j-1]
                up = dp[i-1][j]
                leftup = dp[i-1][j-1]
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = min(left+1 , up+1 , leftup)
                else:
                    dp[i][j] = min(left,up,leftup) + 1

        return dp[m][n]
```
