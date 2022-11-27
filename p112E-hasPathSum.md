> Problem: [112. 路径总和](https://leetcode.cn/problems/path-sum/description/)

# Code

```Python []

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        def check(root,tempsum):
            if not root.left and not root.right:
                if tempsum+root.val == targetSum:
                    return True
                else:
                    return False
            elif not root.left and root.right:
                return check(root.right,tempsum+root.val)
            elif not root.right and root.left:
                return check(root.left,tempsum+root.val)
            else:
                return check(root.right,tempsum+root.val) or check(root.left,tempsum+root.val)
        return check(root,0)




```
