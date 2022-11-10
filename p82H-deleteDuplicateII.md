> Problem: [82. 删除排序链表中的重复元素 II](https://leetcode.cn/problems/remove-duplicates-from-sorted-list-ii/description/)

# 思路

> 链表元素处理，注意边界情况的讨论！！！

# 复杂度

- 时间复杂度: $O(n)$

- 空间复杂度: $O(1)$

# Code

```Python []

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head

        p = ListNode(-101)
        p.next = head
        q = p
        pivot = q
        while p!=None and p.next!=None:
            while(p.next!= None and p.val == p.next.val):
                p = p.next
            p = p.next
            if p == None or p.next == None or p.val != p.next.val:
                q.next = p
                q = p
        return pivot.next
```
