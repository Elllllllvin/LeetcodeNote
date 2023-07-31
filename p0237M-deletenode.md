> Problem: [237. 删除链表中的节点](https://leetcode.cn/problems/delete-node-in-a-linked-list/description/)

[TOC]


# Code
```Python []

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        q = p = node
        while p.next != None:
            p.val = p.next.val
            q = p
            p = p.next
        q.next = None
```
