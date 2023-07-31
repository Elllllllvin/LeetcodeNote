> Problem: [260. 只出现一次的数字 III](https://leetcode.cn/problems/single-number-iii/description/)

[TOC]

# 解题方法
> 位运算

# 复杂度å
- 时间复杂度: $O(n)$

- 空间复杂度: $O(1)$

# Code
```Python3 []

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = 0
        for i in range(n):
            res = res ^ nums[i]

        lsb = res & (-res)
        type1 = type2 = 0
        for i in range(n):
            if nums[i]&lsb:
                type1 ^= nums[i]
            else:
                type2 ^= nums[i]
        
        return [type1,type2]

```
