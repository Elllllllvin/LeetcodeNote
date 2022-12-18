> Problem: [35. 搜索插入位置](https://leetcode.cn/problems/search-insert-position/description/)

# 思路

> 本人比较适合做 Easy 的题 -.-b

# 复杂度

- 时间复杂度: $O(logn)$

- 空间复杂度: $O(1)$

# Code

```Python3 []

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i,j = 0,len(nums)-1
        while(i<=j):
            mid = (i+j)//2
            if(nums[mid]<target):
                i = mid + 1
            elif(nums[mid]>= target):
                j = mid - 1
        return i
```
