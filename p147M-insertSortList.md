> Problem: [147. 对链表进行插入排序](https://leetcode.cn/problems/insertion-sort-list/description/)

[TOC]

# 思路

> 插入排序：每次把后一个元素找到合适的位置插入前面已排好的序列中。

# Code1

- 时间复杂度: $O(n^2)$
- 空间复杂度: $O(1)$

```Python []

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tail = dummy = ListNode(-inf)
        dummy.next = head
        q = head
        while q :
            p = q.next
            if q.val>=tail.val:
                tail.next = q
                tail = tail.next
                tail.next = None
            else:
                pret = dummy
                while pret.next.val < q.val:
                    pret = pret.next
                q.next = pret.next
                pret.next = q
            q = p
        return dummy.next
```
