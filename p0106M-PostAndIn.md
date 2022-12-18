> Problem: [106. 从中序与后序遍历序列构造二叉树](https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/)

# 思路

> 递归！！自己做出来的一遍过 ohhhhhhhhhh

# 复杂度

- 时间复杂度: $O(n^2)$

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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        def build(postorder,inorder):
            if not inorder or not postorder:
                return None
            rootval = postorder[-1]
            curNode = TreeNode(rootval)
            idx = inorder.index(rootval)
            curNode.right = build(postorder[-1-(len(inorder)-idx-1):-1],inorder[idx+1:])
            curNode.left = build(postorder[:-1-(len(inorder)-idx-1)],inorder[:idx])


            return curNode
        return build(postorder,inorder)
```
