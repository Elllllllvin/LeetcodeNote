> Problem: [144. 二叉树的前序遍历](https://leetcode.cn/problems/binary-tree-preorder-traversal/description/)

[TOC]

# 思路

> 1.递归 2.遍历

# Code1 递归

- 时间复杂度: $O(n)$
- 空间复杂度: $O(n)$

```Python []

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(root):
            if not root:
                return
            res.append(root.val)
            dfs(root.left)
            dfs(root.right)

        dfs(root)

        return res

```

# Code2 迭代

```Python []

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        WHITE,GRAY = 0,1
        stack = [(root,WHITE)]
        while stack:
            node,color = stack.pop()
            if node == None:
                continue
            if color == WHITE:
                stack.append((node.right,WHITE))
                stack.append((node.left,WHITE))
                stack.append((node,GRAY))
            elif color == GRAY:
                res.append(node.val)


        return res

```
