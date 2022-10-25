> Problem: [2. 两数相加](https://leetcode.cn/problems/add-two-numbers/description/)

# 思路

> 按位相加，类似计组中的一位加法器，链表的形式给出，不算很难
> 主要通过此题学会如何用 python 的类来实现链表。

# 解题方法

> 设置一个进位标志 carryflag

# 复杂度

击败 92.97%

- 时间复杂度:

  > $O(n)$

- 空间复杂度:
  > 示例： $O(n)$

# Code

```Python []

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l = ListNode()
        head = l
        cf = 0
        while(True):
            s = 0
            s =  l1.val + l2.val + cf
            if s>9:
                s = s-10
                cf = 1
            else :
                cf = 0
            l.val = s
            if l1.next is None and l2.next is None:
                if cf==1:
                    l.next = ListNode(1)
                break
            l.next = ListNode()
            if l1.next is None:
                l1.next = ListNode()
            elif l2.next is None:
                l2.next = ListNode()
            l1 = l1.next
            l2 = l2.next
            l = l.next
        return head

```

# Code：使用 python 实现链表

```Python []



```
