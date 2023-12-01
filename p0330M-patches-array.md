> Problem: [330. 按要求补齐数组](https://leetcode.cn/problems/patching-array/description/)

[toc]

# 思路

> 好难啊！！！！！

# 复杂度

- 时间复杂度:  $O(n)$
- 空间复杂度:  $O(1)$

# Code

```Python
  class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:

        patches = 0
        x = 1
        length = len(nums)
        index = 0

        while x <= n: #能连续覆盖的重量还没到n
            if index < length and nums[index] <= x:
                x += nums[index]
                index += 1
            else:
                x <<= 1
                patches += 1

            # print('x = ',x)
            # print()

        return patches

```
