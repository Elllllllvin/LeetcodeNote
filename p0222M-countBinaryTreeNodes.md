> Problem: [222. 完全二叉树的节点个数](https://leetcode.cn/problems/count-complete-tree-nodes/description/)

[TOC]

# 思路
> 讲述看到这一题的思路

# 解题方法
> 描述你的解题方法

# 复杂度
- 时间复杂度: $O(logn)$

- 空间复杂度: $O(n)$

# Code
```Python []

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        res = []
        WHITE,GRAY = 0,1
        stack = [(WHITE,root)]
        while stack:
            color,node = stack.pop()
            if node == None:
                continue
            if color == WHITE:
                stack.append((WHITE,node.right))
                stack.append((GRAY,node))
                stack.append((WHITE,node.left))
            elif color == GRAY:
                res.append(node.val)

        return len(res)
```
