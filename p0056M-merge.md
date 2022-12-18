> Problem: [56. 合并区间](https://leetcode.cn/problems/merge-intervals/description/)

[TOC]

# 思路

> 讲述看到这一题的思路

# 解题方法

> 排序的妙用

# Code

```Python []

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key=lambda x: x[0])
        for item in intervals:
            if len(res) == 0 :
                res.append(item)
            else:
                if(item[0]<=res[-1][1]):
                    res[-1][1] = max(item[1],res[-1][1])
                else:
                    res.append(item)
        return res
```
