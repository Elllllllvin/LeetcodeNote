> Problem: [48. 旋转图像](https://leetcode.cn/problems/rotate-image/description/)

# 思路

> 1、先根据主对角线进行翻转，在上下垂直翻转，得到结果
> 2、东南西北每四个元素可以组成一个循环

# 解题方法

> 描述你的解题方法

# Code1 对角线翻转 + 垂直翻转

```Python []
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(n-i):
                matrix[i][j],matrix[n-j-1][n-i-1] = matrix[n-j-1][n-i-1],matrix[i][j]

        for i in range(n//2):
            matrix[i],matrix[n-i-1] = matrix[n-i-1],matrix[i]
```

# Code2 每四个元素可以组成一个循环(东南西北)

```Python []
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n // 2):
            for j in range((n + 1) // 2):
                matrix[i][j], matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1] \
                    = matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1], matrix[i][j]
```
