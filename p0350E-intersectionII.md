> Problem: [350. 两个数组的交集 II](https://leetcode.cn/problems/intersection-of-two-arrays-ii/description/)

[toc]

# 思路

> 利用Counter

# 复杂度

- 时间复杂度: $O(n)$
- 空间复杂度: $O(n)$

# Code

```Python3


class Solution:

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        n1,n2 =len(nums1),len(nums2)

        c1 = collections.Counter(nums1)

        c2 = collections.Counter(nums2)

        res = []

        for key,val in c1.items():

            if key in c2:

                res += [key]*min(c1[key],c2[key])

        return res



```
