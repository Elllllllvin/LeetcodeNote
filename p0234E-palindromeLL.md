> Problem: [234. 回文链表](https://leetcode.cn/problems/palindrome-linked-list/description/)

[TOC]

# 思路
> 讲述看到这一题的思路

# 解题方法
> 描述你的解题方法


# Code
```Python3 []

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        res = ''
        p = head
        while p:
            res += str(p.val)
            p = p.next
        
        return res == res[::-1]
```
