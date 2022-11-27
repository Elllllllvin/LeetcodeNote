> Problem: [119. 杨辉三角 II](https://leetcode.cn/problems/pascals-triangle-ii/description/)

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
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        for i in range(1,rowIndex+1):
            cur = [1]
            if i>1:
                for j in range(len(res)-1):
                    cur.append(res[j]+res[j+1])
            res = cur+[1]

        return res

```
