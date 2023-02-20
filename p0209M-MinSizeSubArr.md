_Italic_> Problem: [209. 长度最小的子数组](https://leetcode.cn/problems/minimum-size-subarray-sum/description/)

# 思路

## 方法 1：滑动窗口

## Code1

时间复杂度：o(n)

空间复杂度：o(1)

```Python
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = len(nums)+1
        left, right = 0,0
        s = 0
        while left <= right and right<=len(nums):
            if s < target:
                if right == len(nums):
                    break
                s = s+nums[right]
                right += 1
            else:
                res = min(res,right-left)
                s = s-nums[left]
                left += 1
        if res>len(nums):
            return 0
        else:
            return res
```

## Code2 官方写的滑动窗口，比我的快

```Python[]
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = len(nums)+1
        left, right = 0,0
        s = 0
        while right<len(nums):
            s = s+nums[right]
            while s >= target:
                res = min(res,right-left+1)
                s = s-nums[left]
                left += 1
            right += 1
        if res>len(nums):
            return 0
        else:
            return res



``
```
