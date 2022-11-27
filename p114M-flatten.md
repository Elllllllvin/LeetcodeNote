> Problem: [114. 二叉树展开为链表](https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/description/)

# 思路

> 中序遍历

# Code

```Python []

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        WHITE,GRAY = 0,1
        pre = TreeNode(-1)
        stack = [(root,WHITE)]
        while stack:
            node,color = stack.pop()
            if node == None:
                continue
            if color == WHITE:
                stack.append((node.right,WHITE))
                stack.append((node.left,WHITE))
                stack.append((node,GRAY))
            else: #color = GRAY
                pre.right = node
                pre.left = None
                pre = pre.right

```
