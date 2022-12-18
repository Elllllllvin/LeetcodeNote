> Problem: [21. 合并两个有序链表](https://leetcode.cn/problems/merge-two-sorted-lists/description/)

[TOC]

# 思路

> 合并两个有序链表，类比合并两个有序数组

# 解题方法

> 类比合并两个有序数组

# 复杂度

- 时间复杂度:

  > $O(m+n)$

- 空间复杂度:
  > $O(m+n)$

# Code

82.14% 58.40%

```Python []

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        res = ListNode()
        head = res
        p1 = list1
        p2 = list2
        if(p1 == None and p2 == None):
            return None
        while(p1!=None and p2!=None):
            if(p1.val <= p2.val):
                res.val = p1.val
                p1 = p1.next
                res.next = ListNode(0)
                res = res.next
            else:
                res.val = p2.val
                p2 = p2.next
                res.next = ListNode(0)
                res = res.next
        while(p1 == None and p2!= None):
            res.val = p2.val
            if(p2.next != None):
                res.next = ListNode(0)
                res = res.next
            p2 = p2.next
        while(p2 == None and p1!= None):
            res.val = p1.val
            if(p1.next != None):
                res.next = ListNode(0)
                res = res.next
            p1 = p1.next

        return head



```
