给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。

找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。

说明：你不能倾斜容器。

# COde1 暴力循环法

蠢方法。。超时了。。。

```Python []
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxA = 0
        for i in range(len(height)):
            for j in range(i+1,len(height)):
                t = 0
                if height[j] > height[i]:
                    t = (j-i)*height[i]
                else:
                    t = (j-i)*height[j]
                if t > maxA:
                    maxA = t
        return maxA

```

# Code2 双指针法

比第一种快很多 O(n)

```Python []
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1
        ans = 0
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            ans = max(ans, area)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return ans



```
