> Problem: [382. 链表随机节点](https://leetcode.cn/problems/linked-list-random-node/description/)

[toc]

# 思路

> 只用了简单方法，蓄水池方法是啥？

# 解题方法

# 复杂度

时间复杂度: $O(n)$

空间复杂度: $O(n)$

# Code

```Python

# Definition for singly-linked list.

# class ListNode:

#     def __init__(self, val=0, next=None):

#         self.val = val

#         self.next = next

class Solution:


    def __init__(self, head: Optional[ListNode]):

        self.nums = []

        p = head

        while p!= None:

            self.nums.append(p.val)

            p = p.next

    def getRandom(self) -> int:

        return random.choice(self.nums)



# Your Solution object will be instantiated and called as such:

# obj = Solution(head)

# param_1 = obj.getRandom()

```
