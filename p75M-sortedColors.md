> Problem: [75. 颜色分类](https://leetcode.cn/problems/sort-colors/description/)

# 思路

> 排序算法

# 解题方法

这道题使用快排（性能最好的一种），但是不具有稳定性
[7 大排序方法](https://blog.csdn.net/weixin_44030298/article/details/102641051)

# 复杂度

- 时间复杂度:

  > 添加时间复杂度, 示例： $O(nlogn)$

- 空间复杂度:
  > 添加空间复杂度, 示例： $O(n)$

# Code

```Python []

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def quicksort(nums,start,end):
            if start >= end:
                return
            pivot,left,right = nums[start],start,end
            while left < right:
                while right > left and nums[right] >= pivot:
                    # print(right)
                    right -= 1
                nums[left] = nums[right]
                while right > left and nums[left] < pivot:
                    left += 1
                nums[right] = nums[left]
            nums[left] = pivot
            quicksort(nums,start,left)
            quicksort(nums,left+1,end)
        quicksort(nums,0,len(nums)-1)
```
