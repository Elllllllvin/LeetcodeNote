> Problem: [328. 奇偶链表](https://leetcode.cn/problems/odd-even-linked-list/description/)

[toc]

# 思路

> 我天呢这么简单一道题我写那个复杂，，，虽然做出来了，，，

# 解题方法

> 描述你的解题方法

# 复杂度

- 时间复杂度: $O(n)$

- 空间复杂度:$O(1)$

# Code2 leetcode优化，感觉自己好蠢，，，，

```Python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head :
            return head

        odd = head
        even_head = even = head.next
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        
        return head

```