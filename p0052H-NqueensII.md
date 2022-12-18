> Problem: [52. N 皇后 II](https://leetcode.cn/problems/n-queens-ii/description/)

[TOC]

# 思路

> 把 51 题改了改

# Code

```Python []

class Solution:
    def totalNQueens(self, n: int) -> int:
        def dfs(row):
            if row==n:
                res.append(1)
            else:
                for j in range(n):
                    if j not in col and (row - j) not in posDiagnose and (row + j) not in negDiagnose:
                        queens[row] = j
                        col.add(j)
                        posDiagnose.add(row - j)
                        negDiagnose.add(row + j)
                        dfs(row+1)
                        col.remove(j)
                        posDiagnose.remove(row - j)
                        negDiagnose.remove(row + j)
                    else:
                        continue
        res = []
        col = set()
        posDiagnose = set()
        negDiagnose = set()
        queens = [-1]*n
        dfs(0)

        return len(res)
```
