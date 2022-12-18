> Problem: [15. 三数之和](https://leetcode.cn/problems/3sum/description/)

# 思路

> 双指针法

# 解题方法

> 采用双指针+循环遍历的思想
> 一开始以为循环遍历肯定超时，因此掉入递归的圈套。。结果这题必须要用循环遍历

# 复杂度

- 时间复杂度:

  > 添加时间复杂度, 示例： $O(n^2)$

- 空间复杂度:
  > 添加空间复杂度, 示例： $O(n)$

# Code1 双指针+循环遍历

```Python []

class Solution:
    def threeSum(self, nums):
        nums.sort()
        res, left = [], 0
        for left in range(len(nums) - 2):
            if nums[left] > 0:
                break # .第一个元素就大于0的话不用看了
            if left > 0 and nums[left] == nums[left - 1]:
                continue # 2. skip the same `nums[k]`.
            mid, right = left + 1, len(nums) - 1
            while mid < right: # 3. double pointer
                s = nums[left] + nums[mid] + nums[right]
                if s < 0:
                    mid += 1
                    while mid < right and nums[mid] == nums[mid - 1]:
                        mid += 1
                elif s > 0:
                    right -= 1
                    while mid < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif s == 0:
                    res.append([nums[left], nums[mid], nums[right]])
                    mid += 1
                    right -= 1
                    while mid < right and nums[mid] == nums[mid - 1]:
                        mid += 1
                    while mid < right and nums[right] == nums[right + 1]:
                        right -= 1
        return res

```

# Code2 递归

会超出时间限制

```Python []

class Solution(object):
    def checkthreesum(self,nums,left,mid,right):
        if(mid >= right or left >= right):
            return []
        s = nums[left]+nums[mid]+nums[right]
        res = []
        if( s == 0):
            res += [[nums[left],nums[mid],nums[right]]]
            while(right-1 > mid and nums[right-1]==nums[right]):
                right -= 1
            while(right > mid +1 and nums[mid+1]==nums[mid]):
                mid += 1
            res += self.checkthreesum(nums,left,mid+1,right-1)
        elif s > 0:
            while(right-1 > mid and nums[right-1]==nums[right]):
                right -= 1
            res += self.checkthreesum(nums,left,mid,right-1)
        elif s < 0:
            while(right > mid +1 and nums[mid+1]==nums[mid]):
                mid += 1
            res += self.checkthreesum(nums,left,mid+1,right)
            while(right > left + 2 and nums[left+1]==nums[left]):
                left +=1
            res += self.checkthreesum(nums,left+1,left+2,right)
        return res

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        n = len(nums)
        res += self.checkthreesum(nums,0,1,n-1)
        # print(res)
        res = set((tuple(t) for t in res))
        res = list(res)

        return res


```
