> Problem: [143. 重排链表](https://leetcode.cn/problems/reorder-list/description/)

[TOC]

# 思路

> 链表题！

# Code

```Python []

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        tail = fast = slow = head
        while fast and fast.next:
            tail = slow
            slow = slow.next
            fast = fast.next.next
        # slow 是后半段的头节点
        tail.next = None

        pre = ListNode()
        p = pre.next
        while slow:
            t = slow
            pre.next = slow
            slow = slow.next
            t.next = p
            p = t

        p2 = pre.next
        p1 = head
        t1,t2 = p1,p2
        while p1 and p2:
            t1,t2 = p1,p2
            p1 = p1.next
            p2 = p2.next
            t1.next = t2
            t2.next = p1
            # print(t1.val,t2.val)
        # print(p1,p2)
        if p2:
            t2.next = p2
        return head

```
