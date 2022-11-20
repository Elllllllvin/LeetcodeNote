> Problem: [105. 从前序与中序遍历序列构造二叉树](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/)

# 思路

> > 递归！！自己做出来的一遍过 ohhhhhhhhhh

# 复杂度

- 时间复杂度: $O(n)$

- 空间复杂度: $O(n^2)$
  因为 index 复杂度为 O(n),乘上需要遍历每个节点为 O(n)

# Code

```Python []

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def build(preorder,inorder):
            if not inorder or not preorder:
                return None
            rootval = preorder[0]
            curNode = TreeNode(rootval)
            idx = inorder.index(rootval)
            curNode.left = build(preorder[1:idx+1],inorder[:idx])
            curNode.right = build(preorder[idx+1:],inorder[idx+1:])

            return curNode
        return build(preorder,inorder)
```
