> Problem: [230. 二叉搜索树中第K小的元素](https://leetcode.cn/problems/kth-smallest-element-in-a-bst/description/)

[TOC]

# 思路
> 中序遍历（套公式）

# 复杂度
- 时间复杂度: 最坏$O(n)$，最好O(logn)

- 空间复杂度: 
> 添加空间复杂度, 示例： $O(n)$

# Code
```Python []

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = [(root,1)]
        res = []
        while stack:
            x = stack.pop()
            node,color = x[0],x[1]
            if color == 1:
                if node.right:
                    stack.append((node.right,1))
                stack.append((node,0))
                if node.left:
                    stack.append((node.left,1))
            elif color == 0:
                res.append(node.val)
        return res[k-1]

        



```
