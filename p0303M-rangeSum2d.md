> Problem: [304. 二维区域和检索 - 矩阵不可变](https://leetcode.cn/problems/range-sum-query-2d-immutable/description/)

[toc]

# 思路

二维前缀和

# 复杂度

- 时间复杂度:

>  每次查询$O(1)$，建立二维数组$O(n)$

- 空间复杂度:

>  $O(mn)$

# Code

```Python []


class NumMatrix:


    def __init__(self, matrix: List[List[int]]):

        m,n = len(matrix),len(matrix[0])

        self.mat = [[0]*n for _ in range(m)]

        for i in range(m):

            for j in range(n):  

                self.mat[i][j] = matrix[i][j]

                self.mat[i][j] += self.mat[i-1][j] if i-1>=0 else 0

                self.mat[i][j] += self.mat[i][j-1] if j-1>=0 else 0

                self.mat[i][j] -= self.mat[i-1][j-1] if j>=1 and i>=1 else 0


        # print(self.mat)


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        res = self.mat[row2][col2]

        res -= self.mat[row1-1][col2] if row1>=1 else 0

        res -= self.mat[row2][col1-1] if col1>=1 else 0

        res += self.mat[row1-1][col1-1] if row1 >= 1 and col1>=1 else 0

        return res






# Your NumMatrix object will be instantiated and called as such:

# obj = NumMatrix(matrix)

# param_1 = obj.sumRegion(row1,col1,row2,col2)

```
