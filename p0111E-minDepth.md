> Problem: [111. 二叉树的最小深度](https://leetcode.cn/problems/minimum-depth-of-binary-tree/description/)

# Code

```Python []

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def getHeight(root):
            if not root.left and not root.right:
                return 1
            elif not root.left and root.right:
                return getHeight(root.right)+1
            elif not root.right and root.left:
                return getHeight(root.left)+1
            else:
                leftH = getHeight(root.left)
                rightH = getHeight(root.right)
                return min(leftH,rightH) + 1
        return getHeight(root)

```
