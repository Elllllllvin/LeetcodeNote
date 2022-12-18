> Problem: [45. 跳跃游戏 II](https://leetcode.cn/problems/jump-game-ii/description/)

[TOC]

# 思路

> 贪心算法

# 解题方法

> 通过比较最大能到达的地址和当前地址大小，更新最大能达到的地址，每次都跳到最大的地址

# Code

```Python []

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos #end为当前能到达的最大的地址
                    step += 1
        return step

```
