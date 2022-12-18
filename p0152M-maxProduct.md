> Problem: [152. 乘积最大子数组](https://leetcode.cn/problems/maximum-product-subarray/description/)

[TOC]

# 思路

> 动态规划。。。。

# Code1 动态规划

```Python []

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        pre_max = nums[0]
        pre_min = nums[0]
        for num in nums[1:]:
            cur_max = max(pre_max*num,pre_min*num,num)
            cur_min = min(pre_max*num,pre_min*num,num)
            res = max(res,cur_max)
            pre_max = cur_max
            pre_min = cur_min
        return res
```

# Code2 暴力法直接美美超时

```Python []
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = -inf
        n = len(nums)
        if n == 1:
            return nums[0]
        for i in range(n):
            for j in range(i,n):
                t = 1
                for k in range(i,j+1):
                    t *= nums[k]
                res = max(res,t)
        return res
```
