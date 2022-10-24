> Problem: [16. 最接近的三数之和](https://leetcode.cn/problems/3sum-closest/description/)

# 思路

> 类似于 15 题，排序 + 双指针解法

# 解题方法

> 这题时间卡的没有 15 题紧，15 的基础上稍微改改就过了

# 复杂度

- 时间复杂度:

  > $O(n^2)$

- 空间复杂度:
  > $O(1)$

# Code 排序 + 双指针

```Python []

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res, left = [], 0
        closest = 100000 #最大差距：abs(10000-(-3000)) = 13000
        res = 0
        for left in range(len(nums) - 2):
            mid, right = left + 1, len(nums) - 1
            while mid < right: # 3. double pointer
                s = nums[left] + nums[mid] + nums[right]
                if s < target:
                    mid += 1
                elif s > target:
                    right -= 1
                elif s == target:
                    return nums[left] + nums[mid] + nums[right]

                if abs(target - s) < closest:
                        closest = abs(target - s)
                        res = s
        return res
```
