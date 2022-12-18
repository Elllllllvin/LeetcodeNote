> Problem: [4. 寻找两个正序数组的中位数](https://leetcode.cn/problems/median-of-two-sorted-arrays/description/)

# 思路

> 创建一个目标数组，边排序边合并，最后得到有序数组，求其中位数

# 解题方法

> 由于给定的两个数组均为有序，因此比较两个数组中的元素，较小的放入目标数组中，直到其中一个数组中没有元素，再把另一个数组中剩下的所有元素放到目标数组中，即可完成排序~（‘/’在 python 中仍然是整除（印象中好像‘/’可以直接做浮点数运算。但结果仍是整除。。可能是 python3 中才改过来吧）

# 复杂度

- 时间复杂度:

  > $O(m+n)$

- 空间复杂度:
  > $O(m+n)$

# Code 排序思想

```Python []

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        mergelst = [0]*(len(nums1)+len(nums2))
        i = 0
        j = 0
        k = 0
        while(i < len(nums1) and j < len(nums2)):
            if(nums1[i] <= nums2[j]):
                mergelst[k] = nums1[i]
                i += 1
                k += 1
            else:
                mergelst[k] = nums2[j]
                j += 1
                k += 1
        while(i<len(nums1)):
            mergelst[k] = nums1[i]
            i += 1
            k += 1
        while(j<len(nums2)):
            mergelst[k] = nums2[j]
            j += 1
            k += 1
        n = len(mergelst)
        if n%2==1:
            return mergelst[n//2]
        else:
            return (mergelst[n/2]+mergelst[n/2-1])/2.0
```
