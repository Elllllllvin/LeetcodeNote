> Problem: [145. 二叉树的后序遍历](https://leetcode.cn/problems/binary-tree-postorder-traversal/description/)

[TOC]

# 思路

> 递归，迭代，和上一题一样

# 复杂度

- 时间复杂度: $O(n)$

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
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            dfs(root.right)
            res.append(root.val)
        dfs(root)
        return res

```
