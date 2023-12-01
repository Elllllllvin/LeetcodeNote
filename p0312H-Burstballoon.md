
> Problem: [312. 戳气球](https://leetcode.cn/problems/burst-balloons/description/)

[TOC]

# 思路
> 好难啊！！动态规划！！

# Code
```Python []

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums.insert(0,1)
        nums.append(1)
        n = len(nums)
        dp = [[0]*n for _ in range(n)]

        def range_best(i,j):
            curmax = 0
            #k是(i,j)区间内最后一个被戳的气球,k取值在(i,j)开区间中
            for k in range(i+1,j):
                left = dp[i][k]
                right = dp[k][j]
                curmax = max(curmax,left + nums[i]*nums[k]*nums[j] + right)
            dp[i][j] = curmax
        
        for m in range(2,n):
            #需要对每一个区间长度进行循环，开区间长度从3开始，n从2开始
            for i in range(0,len(nums) - m):
                            #  i+m = len(nums) - 1
                range_best(i,i+m)
        
        return dp[0][len(nums) - 1]

```



``` Python []

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        self.maxres = -1

        def dfs(curres,curnums):
            n = len(curnums)
            if n==0:
                self.maxres = max(self.maxres,curres)
                return
            for i in range(n):
                left = curnums[i-1] if i>0 else 1
                right = curnums[i+1] if i<n-1 else 1
                dfs(curres + curnums[i]*left*right , curnums[:i]+curnums[i+1:])
        
    
        dfs(0,nums[:])
        return self.maxres

```

