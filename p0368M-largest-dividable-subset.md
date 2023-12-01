> Problem: [368. 最大整除子集](https://leetcode.cn/problems/largest-divisible-subset/description/)

[toc]

# 思路

> dp

# 解题方法

> 见解析，不会的话用笔推到一遍

# 复杂度

- 时间复杂度: $O(n^2)$

- 空间复杂度: $O(n)$

# Code

```Python

class Solution:

    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:

        nums.sort()

        n = len(nums)

        f,g = [0]*n , [0]*n

        # f用来存第i个数为结尾的最长「整除子集」长度

        # g用来存f[i]是由哪个下标的状态转移而来，如果f[i]=f[j]+1, 则有g[i]=j

        for i in range(n):

            length,prev = 1,i

            # 起始情况

            for j in range(i):

                if nums[i]%nums[j]==0:

                    # 如果能接在更长的序列后面，则更新f和g

                    if f[j]+1 > length:

                        length = f[j] + 1

                        prev = j

            f[i] = length

            g[i] = prev


        max_len = idx = -1

        for i in range(n):

            if f[i] > max_len:

                idx = i

                max_len = f[i]

            # 找到最大长度和对应下标


        # 适用g回溯出具体方案

        ans = []

        while len(ans) < max_len:

            ans.append(nums[idx])

            idx = g[idx]

        ans.reverse()


        return ans


```
