> Problem: [283. 移动零](https://leetcode.cn/problems/move-zeroes/description/)

[TOC]

# 思路
> 讲述看到这一题的思路

# 解题方法
> 双指针法

# Code
```Python []

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = j = 0
        while j < len(nums):
            if nums[j] == 0:
                j += 1
            else:
                nums[i] = nums[j]
                i += 1
                j += 1
        
        while i<len(nums):
            nums[i] = 0
            i += 1

```
