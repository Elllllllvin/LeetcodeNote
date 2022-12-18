> Problem: [113. 路径总和 II](https://leetcode.cn/problems/path-sum-ii/description/)

# Code

```Python []

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        def check(root,tempsum,path):
            if not root.left and not root.right:
                if tempsum+root.val == targetSum:
                    res.append(path+[root.val])
                    return True
                else:
                    return False
            elif not root.left and root.right:
                check(root.right,tempsum+root.val,path+[root.val])
            elif not root.right and root.left:
                check(root.left,tempsum+root.val,path+[root.val])
            else:
                check(root.left,tempsum+root.val,path+[root.val])
                check(root.right,tempsum+root.val,path+[root.val])
        check(root,0,[])
        return res
```
