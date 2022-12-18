> Problem: [83. 删除排序链表中的重复元素](https://leetcode.cn/problems/remove-duplicates-from-sorted-list/description/)

[TOC]

# 思路

> 链表删除元素

# Code

```Python []

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = q = head
        while p != None:
            while(p.next!= None and p.val == p.next.val):
                p = p.next
            p = p.next
            q.next = p
            q = p
        return head
```
