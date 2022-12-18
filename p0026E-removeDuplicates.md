> Problem: [26. 删除有序数组中的重复项](https://leetcode.cn/problems/remove-duplicates-from-sorted-array/description/)

# 思路

> 把重复的值修改为 10001(题目中元素的最大值+1），再重新排序，前 k 个元素即为答案

# 解题方法

> 把重复的值修改为 10001(题目中元素的最大值+1），再重新排序

# 复杂度

93.26% 65.14%

- 时间复杂度:

  > $O(n)$

- 空间复杂度:
  > $O(1)$

# Code

```Python []

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if(len(nums) == 1):
            return len(nums)
        cnt = 0
        for i in range(len(nums)-1):
            if (nums[i] == nums[i+1]):
                nums[i] = 10001
                cnt += 1
        nums.sort()
        return len(nums)-cnt
```
