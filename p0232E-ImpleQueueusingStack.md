> Problem: [232. 用栈实现队列](https://leetcode.cn/problems/implement-queue-using-stacks/description/)

[TOC]

# 思路
> 讲述看到这一题的思路

# 解题方法
> 描述你的解题方法

# 复杂度
- 时间复杂度: 
> 添加时间复杂度, 示例： $O(n)$

- 空间复杂度: 
> 添加空间复杂度, 示例： $O(n)$

# Code
```Python []

class MyQueue:

    def __init__(self):
        self.list = []

    def push(self, x: int) -> None:
        self.list.append(x)

    def pop(self) -> int:
        res =  self.list.pop(0)
        return res

    def peek(self) -> int:
        return self.list[0]


    def empty(self) -> bool:
        if self.list == []:
            return True
        else:
            return False



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
```
