> Problem: [85. 最大矩形](https://leetcode.cn/problems/maximal-rectangle/description/)

# 思路

> 1.暴力拆解 2.单调栈

# 解题方法

> 描述你的解题方法

# Code1 暴力破解法。。。

# 复杂度

- 时间复杂度: $O(m^2n)$
- 空间复杂度: $O(mn)$

```Python []

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        maxArea = 0
        m,n = len(matrix),len(matrix[0])
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i][j-1] + 1
                else:
                    dp[i][j] = 0

                minwidth = dp[i][j]
                for k in range(i,-1,-1):
                    height = i-k+1
                    minwidth = min(minwidth,dp[k][j])
                    maxArea = max(maxArea,height*minwidth)
        return maxArea
```

# Code2 单调栈（调用上一题的）

```Python []
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        maxArea = 0
        m,n = len(matrix),len(matrix[0])
        heights = [0]*n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0

            maxArea = max(maxArea,self.largestRectangleArea(heights))
        return maxArea

    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = -1
        i = 0
        stack = []
        for i in range(len(heights)):
            while len(stack) > 0 and heights[stack[-1]] > heights[i]:
                cur_height = heights[stack.pop()]

                while len(stack) > 0 and cur_height == heights[stack[-1]]:
                    stack.pop()

                if len(stack) > 0:
                    cur_width = i - stack[-1] - 1
                else:
                    cur_width = i

                maxArea = max(maxArea,cur_height * cur_width)
            stack.append(i)

        while len(stack)>0 is not None:
            cur_height = heights[stack.pop()]

            while len(stack) > 0 and cur_height == heights[stack[-1]]:
                stack.pop()

            if len(stack) > 0:
                cur_width = len(heights) - stack[-1] - 1
            else:
                cur_width = len(heights)

            maxArea = max(maxArea,cur_height * cur_width)

        return maxArea
```
