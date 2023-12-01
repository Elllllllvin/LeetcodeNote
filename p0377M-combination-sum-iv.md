> Problem: [377. 组合总和 Ⅳ](https://leetcode.cn/problems/combination-sum-iv/description/)

[toc]

# 思路

> 动态规划！！！

# 解题方法

> 描述你的解题方法

# 复杂度

- 时间复杂度: $O(n*target)$

- 空间复杂度: $O(target)$

# Code

```Python


class Solution:

    def combinationSum4(self, nums: List[int], target: int) -> int:

        dp = [1] + [0]*target

        for i in range(1,target +1 ):

            for num in nums:

                if num<=i:

                    dp[i] += dp[i-num]

        return dp[target]




```
