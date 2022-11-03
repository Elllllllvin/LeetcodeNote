> Problem: [55. 跳跃游戏](https://leetcode.cn/problems/jump-game/description/)

之前做过一道类似的题，代码其实还能再优化一下，但今天好累啊。。。懒得优化。。。

# Code

```Python []

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxjump = 0
        n = len(nums)
        if n == 1:
            return True

        for i in range(n-1):
            maxjump = max(maxjump,i+nums[i])
            if maxjump == i:
                return False
            if maxjump >= n-1:
                return True
        return False

```
