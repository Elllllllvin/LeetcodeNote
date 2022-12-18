> Problem: [18. 四数之和](https://leetcode.cn/problems/4sum/description/)

三数之和的延申，解法相同

# 复杂度

- 时间复杂度:

  > 添加时间复杂度, 示例： $O(n^3)$

- 空间复杂度:
  > 添加空间复杂度, 示例： $O(logn)$

# Code

```Python []

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        n = len(nums)
        if(n<4):
            return []
        for left in range(n-3):
            if(nums[left] + nums[n-1] + nums[n-2] + nums[n-3]) < target:
                continue
            if left > 0 and nums[left] == nums[left - 1]:
                continue # 2.skip the same `nums[k]`.
            lmid = 0
            for lmid in range(left + 1 , n-2 ):
                if(nums[left] + nums[n-1] + nums[n-2] + nums[lmid]) < target:
                    continue
                if lmid > left + 1 and nums[lmid] == nums[lmid - 1]:
                    continue # 2.skip the same `nums[k]`.
                rmid = lmid + 1
                right = len(nums) - 1
                while(rmid < right):
                    s = nums[left] + nums[lmid] + nums[rmid] + nums[right]
                    if (s == target):
                        res.append([nums[left] , nums[lmid] , nums[rmid] , nums[right]])
                        rmid += 1
                        right -= 1
                        while rmid < right and nums[rmid] == nums[rmid - 1]:
                            rmid += 1
                        while rmid < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif (s > target ):
                        right -= 1
                        while(right > rmid and nums[right] == nums[right+1]):
                            right -= 1
                    elif (s < target):
                        rmid += 1
                        while(rmid < right and nums[rmid] == nums[rmid - 1]):
                            rmid += 1
            print(res)
        return res

```
