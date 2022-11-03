> Problem: [53. 最大子数组和](https://leetcode.cn/problems/maximum-subarray/description/)

# 思路

这题用动态规划

> MD 该用动态规划的时候，我想到的是滑动窗口，改用滑动窗口的时候我又想的是动态规划。。。。。。。。。。。。。。。。。。。。。。

# Code1 O(n)的时间复杂度

- 时间复杂度: $O(n)$

- 空间复杂度: $O(n)$

```Python []

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp =[0]*n
        dp[0] = nums[0]
        for i in range(1,n):
            if dp[i-1]>0:
                dp[i] = dp[i-1]+nums[i]
            else:
                dp[i] = nums[i]

        return max(dp)

```
