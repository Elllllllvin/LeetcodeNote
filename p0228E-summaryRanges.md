> Problem: [228. 汇总区间](https://leetcode.cn/problems/summary-ranges/description/)

[TOC]

# 思路
> 遍历

# 复杂度
- 时间复杂度: $O(n)$

# Code
```Python []

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        res = []
        if n == 0:
            return res
        else:
            left = right = nums[0]
        for i in range(n):
            if i == n-1:
                if left == right:
                    res.append(str(left))
                else:
                    res.append(str(left)+'->'+str(right))
            else:
                if nums[i] == nums[i+1] - 1:
                    right = nums[i+1]
                else:
                    if left == right:
                        res.append(str(left))
                    else:
                        res.append(str(left)+'->'+str(right))
                    left = right = nums[i+1]
        
        return res

```
