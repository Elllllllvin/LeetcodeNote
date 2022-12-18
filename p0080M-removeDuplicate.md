> Problem: [80. 删除有序数组中的重复项 II](https://leetcode.cn/problems/remove-duplicates-from-sorted-array-ii/description/)

# 复杂度

- 时间复杂度: $O(n)$

- 空间复杂度: $O(1)$

# Code

```Python []

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return len(nums)
        cnt = 0
        for i in range(2,len(nums)):
            if nums[i] == nums[i-1] == nums[i-2]:
                nums[i-2] = 10001
                cnt += 1
        nums.sort()
        return len(nums) - cnt

```
