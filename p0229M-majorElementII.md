> Problem: [229. 多数元素 II](https://leetcode.cn/problems/majority-element-ii/description/)

[TOC]

# 思路
> 摩尔投票法，核心思想。当list中有元素大于n//3个，则这种数最多有两个，因为剩下的数必须小于n//3才能满足相加得n得情况

# 复杂度
- 时间复杂度: 
> 添加时间复杂度, 示例： $O(n)$

- 空间复杂度: 
> 添加空间复杂度, 示例： $O(1)$

# Code
```Python []

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        numA = numB  = None
        cntA = cntB = 0
        for num in nums:
            if num == numA:
                cntA += 1
            elif num == numB:
                cntB += 1
            elif numA == None:
                numA = num
                cntA += 1
            elif numB == None:
                numB = num
                cntB += 1
            else:
                cntA -= 1
                cntB -= 1
                if cntA == 0:
                    numA = None
                if cntB == 0:
                    numB = None
        res = []

        if nums.count(numA)> n//3:
            res.append(numA)
        if nums.count(numB)> n//3:
            res.append(numB)

        return res
        

```
