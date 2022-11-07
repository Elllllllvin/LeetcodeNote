> Problem: [73. 矩阵置零](https://leetcode.cn/problems/set-matrix-zeroes/description/)

# 思路

> 使用一个 cnt 记录第 i 列是否出现 0

# 解题方法

> 法一：使用一个 cnt 记录第 i 列是否出现 0
> 法二：使用两个变量记录第 1 行，第 1 列是否出现 0，然后用第 1 行，第 1 列记录每行/列是否出现 0

# 复杂度

- 时间复杂度: $O(mn)$

- 空间复杂度: $O(n)$

# Code1 哥的方法

```Python []

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m,n = len(matrix),len(matrix[0])
        cnt = [0]*n
        for i in range(m):
            if 0 in matrix[i]:
                for j in range(n):
                    if matrix[i][j] == 0:
                        cnt[j] = 1
        for i in range(m):
            if 0 in matrix[i] :
                matrix[i] = [0]*n
                continue
            for j in range(n):
                if cnt[j] == 1:
                    matrix[i][j] = 0
```
