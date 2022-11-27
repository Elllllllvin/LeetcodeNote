> Problem: [108. 将有序数组转换为二叉搜索树](https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/description/)

[TOC]

# 思路

> 没啥好说的。。

# Code

```Python []

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def buildTree(nums):
            if not nums:
                return None
            mid = len(nums)//2
            root = TreeNode(nums[mid])
            root.left = buildTree(nums[:mid])
            root.right = buildTree(nums[mid+1:])
            return root
        return buildTree(nums)
```
