> Problem: [226. 翻转二叉树](https://leetcode.cn/problems/invert-binary-tree/description/)

[TOC]

# 思路
> 利用递归的思想翻转二叉树

# Code
```Python []

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        resroot = TreeNode()
        if root is not None:
            resroot.val = root.val
            resroot.left = self.invertTree(root.right)
            resroot.right = self.invertTree(root.left)
            return resroot
        else:
            return None
        
        return resroot
```
