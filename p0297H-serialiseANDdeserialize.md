> Problem: [297. 二叉树的序列化与反序列化](https://leetcode.cn/problems/serialize-and-deserialize-binary-tree/description/)

[TOC]

# 思路
> 讲述看到这一题的思路

# 解题方法
采用中序遍历，因为转换成的序列中还包含了None结点，因此只需要一种中序遍历就可以确定二叉树结构，deserialize的时候，利用全局lst的pop性质得以完成

# 复杂度
- 时间复杂度:  $O(n)$

- 空间复杂度:  $O(n)$

# Code
```Python []

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return 'None'
        l = self.serialize(root.left)
        r = self.serialize(root.right)
        res = str(root.val)+','+l+','+r

        return res
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data_list = data.split(',')
        def dfs(lst):
            val = lst.pop(0)
            if val == 'None':
                return None
            node = TreeNode(int(val))
            node.left = dfs(lst)
            node.right = dfs(lst)

            return node
        
        return dfs(data_list)

            

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
```
