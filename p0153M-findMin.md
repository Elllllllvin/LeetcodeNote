> Problem: [153. 寻找旋转排序数组中的最小值](https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/description/)

[TOC]

# 思路

> 二分法，之前做过一道类似的题

# 复杂度

- 时间复杂度: $O(logn)$

- 空间复杂度: $O(1)$

# Code

```Python3 []

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        start,end = 0,n-1
        res = inf
        while start <= end:
            mid = (start+end)//2
            if nums[mid]>=nums[start]:
                res = min(res,nums[start])
                start = mid+1
            else:
                res = min(res,nums[mid])
                end = mid

        return res

```
