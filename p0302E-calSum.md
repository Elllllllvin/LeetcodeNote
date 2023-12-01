> Problem: [303. 区域和检索 - 数组不可变](https://leetcode.cn/problems/range-sum-query-immutable/description/)

[TOC]

# 思路
> 讲述看到这一题的思路

# 解题方法
> 描述你的解题方法

# 复杂度
- 时间复杂度: 
> 添加时间复杂度, 示例： $O(n)$

- 空间复杂度: 
> 添加空间复杂度, 示例： $O(n)$

# Code
```Python []

class NumArray:

    def __init__(self, nums: List[int]):
        self.l = nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.l[left:right+1])



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
```
