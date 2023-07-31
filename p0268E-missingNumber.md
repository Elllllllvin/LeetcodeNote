> Problem: [268. 丢失的数字](https://leetcode.cn/problems/missing-number/description/)

[TOC]

# 思路
> 用常规思路解的，其实可以直接用等差数列求和公式- nums的总和直接得到

# 解题方法
> 描述你的解题方法

# 复杂度
- 时间复杂度:  $O(nlogn)$

- 空间复杂度:  $O(1)$

# Code
```Python []

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if i!=nums[i]:
                return i
        return len(nums)
```
