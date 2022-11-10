> Problem: [84. 柱状图中最大的矩形](https://leetcode.cn/problems/largest-rectangle-in-histogram/description/)

# 思路

> 这道题好难啊！！！！用单调栈！！！！

# 解题方法

> 用单调栈，利用 push 和 pop 巧妙地求得 cur_width,遍历高度数组，如果当前高度高于栈中最后一个元素的高度（栈中存的是数组下标），则入栈，否则出栈，将栈中所有高于当前高度的栈都 pop 出来，并且计算以该值（pop 出来的值）作为高度的最大 Area，width 利用 i-stack.pop 计算。

# 复杂度

- 时间复杂度: $O(n)$

- 空间复杂度: $O(n)$

# Code

```Python []

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = -1
        i = 0
        stack = []
        for i in range(len(heights)): #遍历heights数组
            while len(stack) > 0 and heights[stack[-1]] > heights[i]: # 如果heights[i]的值小于栈中最后一个
                cur_height = heights[stack.pop()] #计算以该值作为高度的 最大矩形面积

                while len(stack) > 0 and cur_height == heights[stack[-1]]:
                    stack.pop() #相等的全pop出来

                if len(stack) > 0:
                    cur_width = i - stack[-1] - 1 #求宽度
                else:
                    cur_width = i #表示最后一个元素最小的height，此时i前面所有的值肯定都高于这个值，因此以这个值作为高度时，前面所有都包括

                maxArea = max(maxArea,cur_height * cur_width)#update
            stack.append(i)
        #遍历结束

        while len(stack)>0 is not None: #把栈里剩下的计算一下
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
