> Problem: [104. 二叉树的最大深度](https://leetcode.cn/problems/maximum-depth-of-binary-tree/description/)

# 思路

> dfs

# 解题方法

> 递归函数需要栈空间，而栈空间取决于递归的深度，因此空间复杂度等价于二叉树的高度。

# 复杂度

- 时间复杂度: $O(n)$

- 空间复杂度: $O(height)$

# Code

```Python []

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def dfs(height,root):
            h1,h2 = height,height
            if root.left:
                h1 = dfs(height + 1,root.left)
            if root.right:
                h2 = dfs(height + 1,root.right)
            return max(h1,h2)
        return dfs(1,root)
```
