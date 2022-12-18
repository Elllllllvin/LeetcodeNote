> Problem: [51. N 皇后](https://leetcode.cn/problems/n-queens/description/)

好难啊！！！！

# 思路

> 类比数独游戏，使用回溯算法，重难点在正对角线/负对角线上皇后是否存在的判断

# 解题方法

> 回溯算法：dfs(row)

- col,posDiagnose,negDiagnose 是三个集合，遍历第 row 行的位置，当(row,j)满足条件，则表示将皇后放在这里，与此同时，`col.add(j)`表示第 j 列已经有皇后，后面的皇后不得放到第 j 列；由于在主对角线上的元素行数减列数的值固定，因此用`posDiagnose(row -j)`表示(row,j)所处这一条正对角线上已有皇后；由于在副对角线上的元素行数加列数的值固定，因此用`negDiagnose(row + j)`表示(row,j)所处这一条副对角线上已有皇后。
- 注意在 add 之后，还要还原之前 col，posD，negD 的状态，因为还要放到下一个元素进行 dfs，**这里的 remove 才是真正的回溯算法**

# 复杂度

- 时间复杂度: $O(n!)$

- 空间复杂度: $O(n)$

# Code

```Python []

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def GenerateBoard(): #产生最终答案
            matrix = ['.'*n]*n
            for i in range(len(queens)):
                matrix[i] = matrix[i][:queens[i]] + 'Q' + matrix[i][queens[i]+1:]
            return matrix

        def dfs(row):
            if row==n:
                matrix = GenerateBoard()
                res.append(matrix)
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

        return res
```
