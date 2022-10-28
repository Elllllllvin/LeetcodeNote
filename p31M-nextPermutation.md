> Problem: [31. 下一个排列](https://leetcode.cn/problems/next-permutation/description/)

# 思路

> 解题方法：倒序先找一个最小的作为 left，再在 left 的右边找一个比 left 大的作为 right，交换 left 和 right，再将 left 左边的元素颠倒过来

# 复杂度

- 时间复杂度:

  > $O(n)$

- 空间复杂度:
  > $O(1)$

# Code

```Python []

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = -1
        for i in range(len(nums)-2,-1,-1):
            if (nums[i] >= nums[i+1]):
                continue
            else:
                left = i
                break
        if left >= 0:
            right = len(nums) - 1
            while right >= 0 and nums[left] >= nums[right]:
                right -= 1
            nums[left], nums[right] = nums[right], nums[left]

        left = left + 1
        right = len(nums)-1
        while(left<right):
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
```
