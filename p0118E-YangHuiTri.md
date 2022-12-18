> Problem: [118. 杨辉三角](https://leetcode.cn/problems/pascals-triangle/description/)

[TOC]

# 思路

> 讲述看到这一题的思路

# 解题方法

> 描述你的解题方法

# 复杂度

- 时间复杂度: $O(n^2)$

- 空间复杂度: $O(n)$

# Code

```Python []

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(1,numRows):
            cur = [1]
            if i>1:
                for j in range(len(res[-1])-1):
                    cur.append(res[-1][j]+res[-1][j+1])

            res.append(cur+[1])


        return res

```
