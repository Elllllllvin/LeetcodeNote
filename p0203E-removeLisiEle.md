_Italic_> Problem: [203. 移除链表元素](https://leetcode.cn/problems/remove-linked-list-elements/description/)

# 思路

1.常规循环 2.递归

# Code1

```Python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        q = pivot = ListNode(-1)
        q.next = head
        p = head
        while p!= None:
            if p.val == val:
                q.next = p.next
            else:
                q = p
            p = p.next

        return pivot.next
```

# Code2 递归

```Python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head == None:
            return head
        head.next = self.removeElements(head.next,val)
        if head.val == val:
            return head.next
        else:
            return head
```
