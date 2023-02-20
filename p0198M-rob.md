_Italic_> Problem: [198. 打家劫舍](https://leetcode.cn/problems/house-robber/description/)

# 思路

动态规划题！！！！

循环，每次 dp[i]取当前能偷到的最大的钱数，要么偷这一家，结果是第 i-2 家加上这一家的和，要么不偷这一家，结果仍然是上一家 i-1 的钱，两者取最大值。最后 dp 最后一个即为答案

# Code1

```Python
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1 :
            return nums[0]
        dp = [0]*n
        dp[0]= nums[0]
        dp[1] = max(dp[0],nums[1])
        for i in range(2,n):
            dp[i] = max(dp[i-2]+nums[i],dp[i-1])
        return dp[-1]
```
