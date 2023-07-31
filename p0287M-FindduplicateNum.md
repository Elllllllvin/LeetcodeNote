> Problem: [287. 寻找重复数](https://leetcode.cn/problems/find-the-duplicate-number/description/)

[TOC]

# 思路
1.用sort函数偷懒
2.原地存储

# Code1
```Python []

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        for i in range(n):
            if nums[i] == nums[i+1]:
                return nums[i]

```
