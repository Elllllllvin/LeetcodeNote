> Problem: [88. 合并两个有序数组](https://leetcode.cn/problems/merge-sorted-array/description/)

[TOC]

# 思路

> 脑子生锈了。。。。。

# Code1 双指针法

- 时间复杂度: $O(m+n)$

- 空间复杂度: $O(m+n)$

```Python []

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]

        elif n == 0:
            pass
        else:
            res = []
            i,j = 0,0
            while(i<m and j<n):
                while(i<m and nums2[j]>=nums1[i]):
                    res.append(nums1[i])
                    i += 1
                res.append(nums2[j])
                j += 1
            while(j<n):
                res.append(nums2[j])
                j+=1
            while(i<m):
                res.append(nums1[i])
                i+=1

            for i in range(len(res)):
                nums1[i] = res[i]


```

# Code2 排序

- 时间复杂度: $O(m+n)$

- 空间复杂度: $O(m+n)$

```Python []

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        res = nums1[:m]+nums2
        res.sort()
        print(res)
        for i in range(len(res)):
            nums1[i] = res[i]

```
