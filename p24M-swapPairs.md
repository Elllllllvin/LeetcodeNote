> Problem: [24. 两两交换链表中的节点](https://leetcode.cn/problems/swap-nodes-in-pairs/description/)

# 思路

> 用三个指针进行实现

# 复杂度

- 时间复杂度:

  > $O(n)$

- 空间复杂度:
  > $O(1)$

# Code

```Python []

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        if(p == None):
            return None
        if(p!=None and p.next== None):
            return p
        pivot = ListNode(0)
        pivot.next = head
        res = pivot
        while True:
            if(p == None or p.next==None):
                break
            q = p.next
            p.next = p.next.next
            q.next = p
            pivot.next = q
            pivot = p
            p = p.next
        return res.next

```

# Code2 递归

代码简洁美观

```Python []
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        newHead = head.next
        head.next = self.swapPairs(newHead.next)
        newHead.next = head
        return newHead

```
