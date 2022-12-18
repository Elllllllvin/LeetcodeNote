> Problem: [124. 二叉树中的最大路径和](https://leetcode.cn/problems/binary-tree-maximum-path-sum/description/)

# 思路

> 每个子树内部的最大路径和是我想求的，要找出最大的 这个内部路径肯定是要走这个子树的 root 的，而且是要参考左右子树所提供的最大和的 想捞取子树所提供的最大和，只能走其中一个分支，因为从 root 伸进去子树的路径，**不能拐来拐去，不能占两路便宜** 只能在子树里选一条分支走，那就得判断哪个分支提供的路径和更大 所以每个递归调用都要返回出【提供给父节点的最大路径和】，它用于计算每个递归调用都要算一下的内部最大路径和

# 复杂度

- 时间复杂度: $O(n)$，遍历次数

- 空间复杂度: $O(H)$ 空间复杂度主要取决于递归调用层数，最大层数等于二叉树的高度，最坏情况下，二叉树的高度等于二叉树中的节点个数。

# Code

```Python []

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.MaxSum = -inf
        def dfs(root):
            if not root:
                return 0

            leftGain = dfs(root.left)
            rightGain = dfs(root.right)
            maxGain = root.val + max(0,leftGain,rightGain)
            self.MaxSum = max(self.MaxSum,leftGain+rightGain+root.val,maxGain)

            return maxGain
        dfs(root)
        return self.MaxSum

```
