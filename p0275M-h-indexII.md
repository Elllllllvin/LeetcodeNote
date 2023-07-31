> Problem: [275. H 指数 II](https://leetcode.cn/problems/h-index-ii/description/)

[TOC]

# 思路
> 使用二分法，求最大边界，和上一道题差不多，，，

# 复杂度
- 时间复杂度:  $O(logn)$

- 空间复杂度:  $O(1)$

# Code
```Python []

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # 使用二分法
        n = len(citations)
        l,r = 0,n-1
        while l <= r:
            mid = (l+r)//2
            if citations[mid] >= n - mid:
                r = mid - 1
            else:
                l = mid + 1
        
        return n - (r + 1)
        # 因为r最后判断的位置是在mid左边一个，因此要还原到r本身应该在的位置，故为r+1
```
