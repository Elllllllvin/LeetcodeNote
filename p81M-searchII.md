> Problem: [81. 搜索旋转排序数组 II](https://leetcode.cn/problems/search-in-rotated-sorted-array-ii/description/)

# 思路

> [33. 搜索旋转排序数组](https://leetcode.cn/problems/search-in-rotated-sorted-array/description/) 这一题的延申

# 解题方法

> 添加条件判断，当`nums[l]==nums[r]==nums[mid]`时，线性查找

# 复杂度

- 时间复杂度: 最坏 $O(n)$

- 空间复杂度: $O(1)$

# Code

```Python []

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l,r = 0,len(nums)-1
        while(l <= r):
            mid = (l+r)//2
            if nums[mid] == target:
                return True
            if nums[mid] == nums[l] == nums[r]:
                l += 1
                r -= 1
            elif nums[mid] >= nums[l]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[mid] <= nums[r]: #右有序
                if nums[mid] < target <= nums[len(nums)-1]:
                    l = mid + 1
                else:
                    r = mid -1
        return False



```
