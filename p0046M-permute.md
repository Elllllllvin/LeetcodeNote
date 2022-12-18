> Problem: [46. 全排列 ⭐⭐⭐](https://leetcode.cn/problems/permutations/description/)

[TOC]

# 思路

> 回溯算法，超经典

# Code

```Python []

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp)
                return
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i+1:], tmp + [nums[i]])
        backtrack(nums, [])
        return res
```
