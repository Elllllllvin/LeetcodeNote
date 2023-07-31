> Problem: [240. 搜索二维矩阵 II](https://leetcode.cn/problems/search-a-2d-matrix-ii/description/)

[TOC]



# Code
```Python []

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        x , y = 0 , n - 1
        # Z字形查找
        while x<m and y>=0:
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] < target:
                x += 1
            else:
                y-= 1
        
        return False
```
