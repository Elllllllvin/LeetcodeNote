> Problem: [363. 矩形区域不超过 K 的最大数值和](https://leetcode.cn/problems/max-sum-of-rectangle-no-larger-than-k/description/)

[toc]

# 思路

> 不会，，好难，，，

# 解题方法

> 描述你的解题方法

# 复杂度

- 时间复杂度:

> 添加时间复杂度, 示例： $O(n)$

- 空间复杂度:

> 添加空间复杂度, 示例： $O(n)$

# Code

```Python3


from sortedcontainers import SortedList

class Solution:

    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:

        ans = float("-inf")

        m,n = len(matrix),len(matrix[0])


        for i in range(m): #枚举上边界

            total = [0]*n

            for j in range(i,m): #枚举下边界

                for c in range(n):

                    total[c] += matrix[j][c] # 更新每列的元素和


                totalSet = SortedList([0])

                s = 0

                for v in total:

                    s+=v

                    lb = totalSet.bisect_left(s-k)

                    if lb != len(totalSet):

                        ans = max(ans,s-totalSet[lb])

                    totalSet.add(s)

        return ans 


```
