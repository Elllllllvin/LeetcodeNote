> Problem: [98. 验证二叉搜索树](https://leetcode.cn/problems/validate-binary-search-tree/description/)

# 思路

> 递归。。。。。我好蠢啊!!!

# Code

```Python []

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def Check(root,maxA = float('inf'),minA = float('-inf')):
            if not root:
                return True

            if root.val <= minA or root.val >=maxA:
                return False

            if not Check(root.left,root.val,minA):
                return False
            if not Check(root.right,maxA,root.val):
                return False
            return True
        return Check(root)
```
