> Problem: [300. 最长递增子序列](https://leetcode.cn/problems/longest-increasing-subsequence/description/)

[TOC]

# 思路
1.动态规划,但时间复杂度比较高
2.贪心算法+二分查找
二分查找主要是用于优化时间复杂度

# 解题方法
> 描述你的解题方法

# Code1
时间复杂度 $O(n^{2})$
空间复杂度 $O(n)$
```Python []

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n
        
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i],dp[j]+1)
        
        return max(dp)
```

# Code2
时间复杂度 $O(nlogn)$
空间复杂度 $O(n)$
```Python []

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        res = [nums[0]]
        for i in range(1,n):
            if nums[i] > res[-1]:
                res.append(nums[i])
            else:
                l,r = 0,len(res)-1
                tmp = r
                while l<=r:
                    mid = (l+r)//2
                    if res[mid] >= nums[i]:
                        tmp = mid
                        r = mid - 1
                    else:
                        l = mid + 1
                res[tmp] = nums[i]
        return len(res)
                
```