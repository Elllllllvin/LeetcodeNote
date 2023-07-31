> Problem: [278. 第一个错误的版本](https://leetcode.cn/problems/first-bad-version/description/)

[TOC]

# 思路
> 二分法

# Code
```Python []

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l,r = 1,n
        while l<=r:
            mid = (l+r)//2
            if isBadVersion(mid):
                r = mid - 1 
            else:
                l = mid + 1
        
        return l
```
