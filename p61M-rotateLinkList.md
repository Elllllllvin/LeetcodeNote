> Problem: [61. 旋转链表](https://leetcode.cn/problems/rotate-list/description/)

[TOC]

# 思路

> 思路就是旋转列表。。自己过的别管了 👉👈

# Code

```Python []
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        tail = p = head
        n = 0
        while p != None:
            n += 1
            tail = p
            p = p.next

        if n < 2 or k%n == 0 :
            return head

        k = k%n
        q = p = head
        for i in range(n-k):
            q = p
            p = p.next
        tail.next = head
        head = p
        q.next = None
        return head

```
