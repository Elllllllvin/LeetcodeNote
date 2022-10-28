> Problem: [33. 搜索旋转排序数组](https://leetcode.cn/problems/search-in-rotated-sorted-array/description/)

# Code1 偷懒尊。。。

```Python []

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        else:
            return nums.index(target)
```

# Code2 二分法查找

```Python []
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l , r = 0 , len(nums)-1
        while l <= r:
            mid = (l + r) //2
            if(nums[mid]== target):
                return mid
            if (nums[0]<=nums[mid]): #有序
                if nums[0]<=target<nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[len(nums)-1]:
                    l = mid + 1
                else:
                    r = mid -1
        return -1
```
