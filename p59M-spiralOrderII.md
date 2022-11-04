> Problem: [59. 螺旋矩阵 II](https://leetcode.cn/problems/spiral-matrix-ii/description/)

[TOC]

# 思路

> 一把过！！哦买噶！！！！！

# 复杂度

- 时间复杂度: $O(n)$

- 空间复杂度: $O(n^2)$

# Code

```Python []

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0]*n for i in range(n)]
        left,right,top,bottom = 0,n-1,0,n-1
        cnt = 0
        while left < right:
            i,j = top,left
            while(j<right):
                cnt += 1
                matrix[i][j] = cnt
                j += 1
            while(i<bottom):
                cnt += 1
                matrix[i][j] = cnt
                i += 1
            while(j>left):
                cnt += 1
                matrix[i][j] = cnt
                j -= 1
            while(i>top):
                cnt += 1
                matrix[i][j] = cnt
                i -= 1
            left,right,top,bottom = left+1,right-1,top+1,bottom-1
        if(left == right):
            cnt += 1
            matrix[left][right] = cnt
        return matrix
```
