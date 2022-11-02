> Problem: [42. 接雨水](https://leetcode.cn/problems/trapping-rain-water/description/)

[TOC]

# 解题方法

- 1.动态规划
- 2.双指针
- 3.单调栈

# Code1 动态规划

- 时间复杂度: $O(n)$

- 空间复杂度: $O(n)$

```Python []

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftMax = [0 for i in range(n)]
        rightMax = [0 for i in range(n)]
        for i in range(n):
            if(i==0):
                leftMax[i] = height[i]
            elif(i>0):
                leftMax[i] = max(leftMax[i-1],height[i])
        for i in range(n-1,-1,-1):
            if(i<n-1):
                rightMax[i] = max(rightMax[i+1],height[i])
            elif(i == n-1):
                rightMax[i] = height[i]
        res = 0
        for i in range(n):
            if height[i]<leftMax[i] and height[i]<rightMax[i]:
                res += min(leftMax[i],rightMax[i])-height[i]

        return res

```

# Code2 双指针

- 时间复杂度: $O(n)$

- 空间复杂度: $O(n)$

```Python []
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        i,j = 0,n-1
        leftMax , rightMax = 0,0
        res = 0
        while(i<j):
            leftMax = max(leftMax,height[i])
            rightMax = max(rightMax,height[j])
            if height[i]<height[j]:
                res += leftMax-height[i]
                i+=1
            else:
                res += rightMax-height[j]
                j-=1

        return res
```

# Code3 单调栈

- 时间复杂度: $O(n)$

- 空间复杂度: $O(n)$

```Python []
class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        stack = list()
        n = len(height)

        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                currWidth = i - left - 1
                currHeight = min(height[left], height[i]) - height[top]
                ans += currWidth * currHeight
            stack.append(i)

        return ans

```
