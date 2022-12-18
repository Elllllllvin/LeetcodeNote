> Problem: [27. 移除元素](https://leetcode.cn/problems/remove-element/description/)

[TOC]

# 思路

> 因为只看前 k 项，需要移除的元素全放后面

# 解题方法

> 把需要移除的元素赋值为 101，重新排序

# 复杂度

- 时间复杂度:

  > $O(n)$

- 空间复杂度:
  > $O(1)$

# Code

```Python []

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cnt = 0
        for i in range(len(nums)):
            if(nums[i] == val):
                cnt += 1
                nums[i] = 101
        nums.sort()
        return len(nums)-cnt
```
