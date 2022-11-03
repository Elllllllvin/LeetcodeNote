> Problem: [57. 插入区间](https://leetcode.cn/problems/insert-interval/description/)

[TOC]

# 思路

> 讲述看到这一题的思路

# 解题方法

> 模拟，分类讨论

# 复杂度

- 时间复杂度: $O(n)$

- 空间复杂度: $O(n)$

# Code 1 自己想出来的

```Python []

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        insertindex = -1
        endindex = -1
        res = []
        for i in range(len(intervals)):
            if newInterval[0]>intervals[i][1]:
                continue
            else:
                if newInterval[1]<intervals[i][0]:
                    res = intervals[:i] + [newInterval] + intervals[i:]
                    return res
                else:
                    insertindex = i
                    intervals[i][0] = min(intervals[i][0],newInterval[0])
                    intervals[i][1] = max(intervals[i][1],newInterval[1])
                    res += intervals[:insertindex+1]
                    break

        if( insertindex == -1):
            res = intervals + [newInterval]
            return res

        for i in range(insertindex+1,len(intervals)):
            if newInterval[1]>intervals[i][1]:
                continue
            elif newInterval[1]<=intervals[i][1]:
                if intervals[insertindex][1]<intervals[i][0]:
                    endindex = i
                    break
                else:
                    intervals[insertindex][1] = intervals[i][1]
                    endindex = i+1
                    break
        if (endindex != -1):
            res += intervals[endindex:]
        return res

```

## Code2 官方

```Python []
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = newInterval
        placed = False
        ans = list()
        for li, ri in intervals:
            if li > right:
                # 在插入区间的右侧且无交集
                if not placed:
                    ans.append([left, right])
                    placed = True
                ans.append([li, ri])
            elif ri < left:
                # 在插入区间的左侧且无交集
                ans.append([li, ri])
            else:
                # 与插入区间有交集，计算它们的并集
                left = min(left, li)
                right = max(right, ri)

        if not placed:
            ans.append([left, right])
        return ans

```
