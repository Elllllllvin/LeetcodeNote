> Problem: [349. 两个数组的交集](https://leetcode.cn/problems/intersection-of-two-arrays/description/)

[toc]

# 思路

> 太简单了

# 解题方法

> 描述你的解题方法

# 复杂度

- 时间复杂度:

> 添加时间复杂度, 示例： $O(n)$

- 空间复杂度:

> 添加空间复杂度, 示例： $O(n)$

# Code

```Python3


class Solution:

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        return list(set([i for i in nums1 if i in nums2]))

```
